# coding=utf-8
from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from extuser.models import ExtUser

from usermedia.models import Photo


# Базовые классы

class BaseComment(models.Model):
    user = models.ForeignKey(ExtUser)

    content = models.CharField(
        u'Текст комментария',
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

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        abstract = True

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id


class Event(models.Model):
    creator = models.ForeignKey(ExtUser)

    participants = models.ManyToManyField(ExtUser)

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


class BaseLike(models.Model):
    user = models.ForeignKey(ExtUser)

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
        abstract = True

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id


class PhotoComment(BaseComment):
    photo = models.ForeignKey(Photo)
    pass


class PhotoLike(BaseLike):
    photo = models.ForeignKey(Photo)
    pass


class CommentLike(BaseLike):
    comment = models.ForeignKey(Comment)
    pass


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')


class Like(models.Model):
    content_type = models.ForeignKey(ContentType)
    content_object = GenericForeignKey('content_type', 'object_id')
