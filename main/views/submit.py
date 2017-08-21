from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from rules import test_rule

from main.models import Submit
from main.serializers import SubmitSerializer
from main.tasks import judge_submit


class SubmitList(generics.CreateAPIView):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        submit = serializer.save()
        judge_submit.delay(submit.pk)


class SubmitDetail(generics.RetrieveAPIView):
    queryset = Submit.objects.all()
    serializer_class = SubmitSerializer
    permission_classes = (IsAuthenticated,)

    def check_object_permissions(self, request, submit):
        if not test_rule('can_view_submit', request.user, submit):
            raise PermissionDenied
