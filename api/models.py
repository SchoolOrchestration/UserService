from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='Profile')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {} ".format(self.team, self.user)
