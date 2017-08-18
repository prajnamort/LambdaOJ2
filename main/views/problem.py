from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from rules import test_rule

from main.models import Problem
from main.serializers import ProblemSerializer


class ProblemList(generics.ListAPIView):
    serializer_class = ProblemSerializer

    def get_queryset(self):
        user = self.request.user
        if test_rule('can_access_unreleased_problems', user):
            return Problem.objects.all()
        else:
            return Problem.objects.filter(released=True)


class ProblemDetail(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def check_object_permissions(self, request, problem):
        if not test_rule('can_access_problem', request.user, problem):
            raise PermissionDenied
