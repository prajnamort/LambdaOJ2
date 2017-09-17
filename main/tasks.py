from django.db import transaction, OperationalError
from django.db.models import F, Q
from django.conf import settings
from django.utils import timezone
from celery import shared_task

import os
import shutil
import string, random
from datetime import timedelta

import oj
from main.judge import run_judge_in_docker, JudgeError
from main.models import Submit
from main.utils.string_utils import generate_noise
from main.utils.directory import remkdir


class CheckConditionError(Exception):
    """自定义错误，用于条件检查错误时。"""
    pass


@shared_task(autoretry_for=(OperationalError, CheckConditionError, JudgeError),
             retry_kwargs={'countdown': 10, 'max_retries': 3})
def judge_submit(submit_pk):
    submit = Submit.objects.get(pk=submit_pk)
    problem = submit.problem

    # 准备文件夹与映射关系
    judge_dir = os.path.join(settings.JUDGE_BASE_DIR,
                             '%s_%s' % (str(submit.id), generate_noise(6)))
    remkdir(judge_dir)
    submit.copy_code_to_dir(judge_dir)
    problem.prepare_problem_dir(judge_dir)
    docker_judge_dir = '/' + generate_noise(8)
    volumes = {judge_dir: {'bind': docker_judge_dir, 'mode': 'ro'}}
    default_check = bool(not problem.compare_file)
    ta_check_file = '' if default_check else os.path.join(docker_judge_dir, 'compare.py')

    # 更新状态为判题中
    with transaction.atomic():
        submit.refresh_from_db()
        if submit.judge_status in [Submit.JUDGE_COMPLETED, Submit.JUDGE_FAILED]:
            raise CheckConditionError('Submit has already been judged.')
        submit.judge_status = Submit.JUDGE_JUDGING
        submit.save()

    try:
        (compile_status, results) = run_judge_in_docker(
            image=settings.JUDGE_DOCKER_IMAGE,
            src_path=os.path.join(docker_judge_dir, submit.codefile_name),
            compiler=submit.get_compiler_name(),
            test_case_dir=docker_judge_dir,
            sample_num=problem.testdata_num,
            mem_limit=problem.memory_limit,
            time_limit=problem.time_limit,
            volumes=volumes,
            max_wait_time=max(60, problem.time_limit * problem.testdata_num + 30),
            default_check=default_check,
            ta_check_file=ta_check_file,)
        shutil.rmtree(judge_dir)
    except JudgeError as e:
        shutil.rmtree(judge_dir)
        submit.judge_status = Submit.JUDGE_PENDING
        submit.save()
        raise e
    except Exception as e:
        shutil.rmtree(judge_dir)
        submit.judge_status = Submit.JUDGE_FAILED
        submit.save()
        raise e

    with transaction.atomic():
        submit.refresh_from_db()
        if submit.judge_status != Submit.JUDGE_JUDGING:
            raise CheckConditionError('Submit is not in JUDGING state.')
        # 更新 Submit 状态和结果
        if compile_status == oj.consts.COMPILE_OK:
            submit.compile_status = Submit.COMPILE_OK
            submit.run_results = [list(tp) for tp in results]
            total = len(submit.run_results)
            accepted = len([status for (status, _, _) in submit.run_results
                            if status == oj.consts.ACCEPTED])
            if total == 0:
                submit.score = 0.0
            else:
                submit.score = 100.0 * (accepted / total)
        elif compile_status == oj.consts.COMPILE_ERROR:
            submit.compile_status = Submit.COMPILE_ERROR
            submit.error_message = results.replace('\x00', '')
            submit.score = 0.0
        submit.judge_status = Submit.JUDGE_COMPLETED
        submit.save()
        # 更新 Problem 统计数据
        problem.submit_cnt = F('submit_cnt') + 1
        if submit.score == 100.0:
            problem.accept_cnt = F('accept_cnt') + 1
        problem.save()


@shared_task
def auto_cancel_unfinished_submits():
    past_time = timezone.now() - timedelta(seconds=3600)
    unfinished_submits = Submit.objects.filter(Q(judge_status=Submit.JUDGE_PENDING) |
                                               Q(judge_status=Submit.JUDGE_JUDGING))\
                                       .filter(create_time__lte=past_time)
    for submit in unfinished_submits:
        submit.judge_status = Submit.JUDGE_FAILED
        submit.save()
