from django.conf import settings

from oj import Judge
from main.models import Problem


class DefaultJudge(Judge):

    def __init__(self, **kwargs):
        problem = Problem.objects.get(pk=kwargs['problem_id'])
        self.testdatas = list(problem.testdata_set.order_by('order'))
        kwargs['sample_num'] = len(self.testdatas)
        kwargs['time_limit'] = problem.time_limit
        kwargs['mem_limit'] = problem.memory_limit
        kwargs['judge_exe']=settings.JUDGE_BIN
        kwargs['compile_code_exe']=settings.COMPILE_CODE_BIN
        super().__init__(**kwargs)

    def get_test_input_by_id(self, id):
        return self.testdatas[id].input_file.path

    def get_std_answer_by_id(self, id):
        return self.testdatas[id].output_file.path

    def check_answer(self, fn1, fn2):
        f1 = open(fn1, "r")
        f2 = open(fn2, "r")
        result = (f1.read() == f2.read())
        f1.close()
        f2.close()
        return result
