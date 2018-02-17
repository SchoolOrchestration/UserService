from rest_framework import serializers


class UserLogin(object):
    def __init__(self, username="", password=""):
        self.password = password
        self.username = username


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, required=True)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        return instance

    def create(self, validated_data):
        return UserLogin(**validated_data)
