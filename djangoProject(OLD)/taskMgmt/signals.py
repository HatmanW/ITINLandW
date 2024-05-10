# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

# Signal to create or update profile when user is created
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

# Connect the signal to the User model's post_save event
post_save.connect(create_or_update_user_profile, sender=User)