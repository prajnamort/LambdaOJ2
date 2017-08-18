from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import Submit
from main.serializers import SubmitSerializer


class SubmitList(generics.CreateAPIView):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer
    permission_classes = (IsAuthenticated,)


class SubmitDetail(generics.RetrieveAPIView):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer
    permission_classes = (IsAuthenticated,)
