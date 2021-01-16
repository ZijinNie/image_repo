from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from user.models import Profile


# create a user profile when creating a user
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        obj = Profile.objects.create(user=instance)
        obj.save()
