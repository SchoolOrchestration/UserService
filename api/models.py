from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    permissions = models.ManyToManyField(Permission, through='TeamPermissions')

    def __str__(self):
        return self.name


class TeamPermissions(models.Model):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
