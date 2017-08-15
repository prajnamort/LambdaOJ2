from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import Problem
from main.serializers import ProblemSerializer


class ProblemList(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticated,)


class ProblemDetail(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = (IsAuthenticated,)
