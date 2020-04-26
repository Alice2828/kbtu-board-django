from datetime import datetime

from rest_framework import serializers

from users.models import User, TeacherInfo


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = TeacherInfo
        fields = '__all__'


class Code(serializers.ModelSerializer):

    class Meta:
        model = TeacherInfo
        fields = '__all__'
