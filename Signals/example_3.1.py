from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import UserProfile

@reciver(post_save, sender = UserProfile)
def user_profile_created(sender, instance, created, **kwargs):
    if created:
        print(f"new user profile created for user : {instance.user.username}")


'''

In this example, when a UserProfile object is created in a Django application,
the user_profile_created function is automatically called, allowing you to perform
actions in response to the event.

'''
