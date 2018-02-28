from django.db.models.signals import post_save
from django.dispatch import receiver
from .kong import Consumer
from .models import (
    Organization,
    Team
)


@receiver(post_save, sender=Organization)
def create_kong_consumer(instance, created, **kwargs):
    if created:
        Consumer.create(instance.name)
