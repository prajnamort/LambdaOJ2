from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import User, Submit
from main.serializers import UserSerializer, SubmitSerializer


class MyInfo(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class MySubmitList(generics.ListAPIView):
    serializer_class = SubmitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Submit.objects.filter(user=self.request.user)
