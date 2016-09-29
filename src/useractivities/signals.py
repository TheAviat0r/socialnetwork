from django.db.models.signals import post_save
from django.dispatch import receiver

from useractivities.models import CommentLike, PhotoComment


@receiver(post_save, sender=CommentLike)
def like_up(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        comment = PhotoComment.objects.get(id=instance.comment)
        comment.count_likes += 1
