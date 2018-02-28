from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Organization,
    Permission,
    Team
)


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


class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ('name', 'code')


class TeamSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Team
        fields = ('name', 'permissions')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    organizations = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'id', 'organizations')

    @staticmethod
    def get_organizations(obj):
        organization_list = []
        for org in obj.organization_set.all():
            org_object = dict()
            org_object['c'] = org.name
            org_object['id'] = org.id
            org_object['groups'] = []
            for team in org.team_set.filter(users=obj.id):
                serialized = TeamSerializer(team)
                org_object['groups'].append(serialized.data)
            organization_list.append(org_object)
        return organization_list

