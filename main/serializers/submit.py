from rest_framework import serializers

from rules import test_rule

from main.models import Submit, Problem


class SubmitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        label='用户',
        default=serializers.CurrentUserDefault(),
        read_only=True,)
    user_username = serializers.SerializerMethodField()
    problem = serializers.SlugRelatedField(
        label='问题',
        queryset=Problem.objects.all(),
        slug_field='number',)

    class Meta:
        model = Submit
        fields = ('id', 'user', 'user_username', 'problem', 'language', 'code',
                  'judge_status', 'compile_status', 'run_results',
                  'error_message', 'score', 'create_time',)
        read_only_fields = ('judge_status', 'compile_status', 'run_results',
                            'error_message', 'score', 'create_time',)

    def validate(self, data):
        if not test_rule('can_access_problem', data['user'], data['problem']):
            raise serializers.ValidationError('您没有提交该问题的权限。')
        return data

    def get_user_username(self, submit):
        return submit.user.username
