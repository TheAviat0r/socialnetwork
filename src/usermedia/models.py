from __future__ import unicode_literals

from django.db import models

# Create your models here.
from extuser.models import ExtUser


def upload_photos(obj, filename):
    to = obj.user.email + "/" + "photo" + "/" + filename
    return to


class Photo(models.Model):
    album = models.ForeignKey(Album)

    description = models.CharField(
        u'Описание',
        max_length=255,
        default=None
    )

    added_at = models.DateField(
        u'Дата добавления',
        auto_now_add=True
    )

    photo = models.ImageField(
        u'Фотография',
        blank=True,
        null=True,
        upload_to=upload_photos
    )


class Album(models.Model):
    user = models.ForeignKey(ExtUser)

    created_at = models.DateField(
        u'Дата создания',
        auto_now_add=True
    )

    description = models.CharField(
        u'Название',
        max_length=40,
        default=None
    )

    description = models.CharField(
        u'Описание',
        max_length=255,
        default=None
    )

    preview = models.OneToOneField(Photo)
