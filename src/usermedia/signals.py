from django.db.models.signals import post_save
from django.dispatch import receiver
from useractivities.models import PhotoComment

from usermedia.models import Photo

from useractivities.models import PhotoLike


@receiver(post_save, sender=PhotoComment)
def comment_up(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        photo = Photo.objects.get(id=instance.photo)
        photo.count_comments += 1


@receiver(post_save, sender=PhotoLike)
def like_up(sender, **kwargs):
    if kwargs["created"]:
        instance = kwargs["instance"]
        photo = Photo.objects.get(id=instance.photo)
        photo.count_likes += 1
