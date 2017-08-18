from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from main.models import User
from main.serializers import UserSerializer


class MyInfo(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
