from django.contrib.auth.models import Group, User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def post_save_user(sender, instance, **kwargs):
    bacon = Group.objects.get(name='bacon')
    instance.groups.add(bacon)
    print('ALl ok')