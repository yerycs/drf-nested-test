from rest_framework import serializers
from django.contrib.auth.models import User
from project.models import Private_ID_Info

class PrivateIDInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Private_ID_Info
        fields = ('first_name', 'last_name', )

class UserInfoSerializer(serializers.ModelSerializer):
    privateIdInfo = PrivateIDInfoSerializer(many=True, read_only=True, source='private_id_info_set')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'privateIdInfo', )