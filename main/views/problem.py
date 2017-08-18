from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rules import test_rule

from main.models import Problem
from main.serializers import ProblemSerializer


class ProblemList(generics.ListAPIView):
    serializer_class = ProblemSerializer

    def get_queryset(self):
        user = self.request.user
        # TODO: is_authenticated
        if user.is_authenticated() and test_rule('can_access_unreleased_problems', user):
            return Problem.objects.all()
        else:
            return Problem.objects.filter(released=True)


class ProblemDetail(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    # permission_classes = (IsAuthenticated,)
