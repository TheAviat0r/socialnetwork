# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

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


def upload_photos(obj, filename):
    to = obj.user.email + "/" + "photo" + "/" + filename
    return to


class Photo(models.Model):
    album = models.ForeignKey(Album)

    preview = models.BooleanField(
        u'Превью',
        default=False
    )

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

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id
