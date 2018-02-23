from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .kong import Consumer
from .models import (
    Organization,
    Profile,
    Team
)


@receiver(post_save, sender=Organization)
def create_kong_consumer(instance, created, **kwargs):
    if created:
        Consumer.create(instance.name)
        admin_team = Team.objects.create(
            name="{}.admin".format(instance.name.lower()),
            organization=instance
        )
        admin_user = User.objects.create_user(
            username="{}_admin".format(instance.name.lower())
        )
        Profile.objects.create(
            user=admin_user,
            team=admin_team
        )
