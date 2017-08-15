from rest_framework import serializers

from main.models import Submit


class SubmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Submit
        fields = ('id', 'problem', 'language', 'code', 'create_time',)
        read_only_fields = ('create_time',)
