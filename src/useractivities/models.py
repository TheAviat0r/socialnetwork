# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.


class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

    content = models.CharField(
        u'Текст комментария',
        default=None,
        max_length=255
    )

    created_at = models.DateTimeField(
        u'Создан',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        u'Обновлен',
        auto_now=True
    )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'


class Event(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)

    name = models.CharField(
        u'Название события',
        max_length=255
    )

    description = models.TextField(
        u'Описание',
        default=u'Создатель события, увы, ещё не оставил его описания'
    )

    duration = models.TimeField(
        u'Длительность мероприятия',
        default=None
    )

    when = models.DateTimeField(
        u'Когда',
        default=None
    )

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'
        abstract = True

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
