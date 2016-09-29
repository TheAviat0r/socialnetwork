from django.db.models.signals import post_save
from django.dispatch import receiver
from useractivities.models import Comment, Like


@receiver(post_save, sender=Comment)
def comment_up(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        obj = instance.content_type.get_object_for_this_type(id=instance.object_id)
        obj.count_comments += 1


@receiver(post_save, sender=Like)
def like_up(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        obj = instance.content_type.get_object_for_this_type(id=instance.object_id)
        obj.count_likes += 1