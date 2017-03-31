from rest_framework import routers, serializers, viewsets

from main.models import Problem
from main.serializers import ProblemSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
