from rest_framework import serializers

from main.models import Problem


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('number', 'title', 'time_limit', 'memory_limit',
                  'desc', 'input_desc', 'output_desc',
                  'input_sample', 'output_sample', 'hint',
                  'sample_num', 'deadline', 'released', 'contributor',
                  'create_time',)
        read_only_fields = ('create_time',)
