from rest_framework import serializers

from main.models import Problem


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Problem
        fields = ('order', 'title', 'time_limit', 'memory_limit')
