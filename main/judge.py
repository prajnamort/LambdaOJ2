from django.conf import settings

from oj import Judge
from main.models import Problem


class DefaultJudge(Judge):

    def __init__(self, **kwargs):
        problem = Problem.objects.get(pk=kwargs['problem_id'])
        self.problem = problem
        self.testdatas = list(problem.testdata_set.order_by('order'))
        kwargs['sample_num'] = len(self.testdatas)
        kwargs['time_limit'] = problem.time_limit
        kwargs['mem_limit'] = problem.memory_limit
        kwargs['judge_exe'] = settings.JUDGE_BIN
        kwargs['compile_code_exe'] = settings.COMPILE_CODE_BIN
        super().__init__(**kwargs)

    def get_test_input_by_id(self, id):
        return self.testdatas[id].input_file.path

    def get_std_answer_by_id(self, id):
        return self.testdatas[id].output_file.path

    def check_answer(self, std_answer, submit_output):
        compare_func = self.problem.compare_func
        return compare_func(std_answer, submit_output)
