from rest_framework import serializers

from main.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile', 'student_id',
                  'is_staff', 'date_joined',)
        read_only_fields = ('date_joined',)
