from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import DerppitUser

@receiver(post_save, sender=User)
def create_derppit_user(sender, instance, created, **kwargs):
    if created:
        DerppitUser.objects.create(user=instance)