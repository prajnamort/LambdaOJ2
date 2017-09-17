import json
import docker

from django.conf import settings


class JudgeError(Exception):
    pass


def run_judge_in_docker(image, src_path, compiler, test_case_dir, sample_num,
                        mem_limit, time_limit, volumes, max_wait_time=60,
                        default_check=True, ta_check_file=''):
    client = docker.from_env()
    command = [
        settings.JUDGE_DOCKER_COMMAND,
        '--src', src_path,
        '--compiler', compiler,
        '--work_dir', '/tmp',
        '--test_case_dir', test_case_dir,
        '--sample_num', str(sample_num),
        '--mem_limit', str(mem_limit),
        '--time_limit', str(time_limit),]
    if default_check:
        command.append('--default_check')
    else:
        command.extend(['--ta_check_file', ta_check_file])

    c = client.containers.run(
        image=image,
        command=command,
        user=settings.JUDGE_DOCKER_USER,
        privileged=True,
        detach=True,
        volumes=volumes,)

    try:
        c.wait(timeout=max_wait_time)
        r = json.loads(c.logs().decode('utf8'))
        c.remove(force=True)
        return r
    except:
        c.remove(force=True)
        raise JudgeError()
