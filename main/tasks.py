from django.db import transaction, OperationalError
from django.db.models import F
from django.conf import settings
from celery import shared_task

import os
import shutil

import oj
from main.judge import run_judge_in_docker
from main.models import Submit


class CheckConditionError(Exception):
    """自定义错误，用于条件检查错误时。"""
    pass


@shared_task(autoretry_for=(oj.judge.NeedRejudgeError,
                            OperationalError,
                            CheckConditionError),
             retry_kwargs={'countdown': 10, 'max_retries': 5})
def judge_submit(submit_pk):
    submit = Submit.objects.get(pk=submit_pk)
    problem = submit.problem
    JudgeClass = DefaultJudge

    # 初始化工作目录
    work_dir = os.path.join(settings.JUDGE_BASE_DIR, str(submit.id))
    if os.path.exists(work_dir):
        shutil.rmtree(work_dir)
    os.mkdir(work_dir)
    source_code = os.path.join(work_dir, 'source%s' % submit.get_codefile_suffix())
    with open(source_code, 'w') as f:
        f.write(submit.code)

    # 更新状态为判题中
    with transaction.atomic():
        submit.refresh_from_db()
        if submit.judge_status in [Submit.JUDGE_COMPLETED, Submit.JUDGE_FAILED]:
            raise CheckConditionError('Submit has already been judged.')
        submit.judge_status = Submit.JUDGE_JUDGING
        submit.save()

    #prepare arguments
    #TODO
    (compile_status, results) = run_judge_in_docker(image, xxxx, xxx, xxx)
     
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
