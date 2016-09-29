# coding=utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
from usermedia.models import WithLike, WithComment

from usermedia.models import Photo


class WithContentType(models.Model):
    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id

    class Meta:
        abstract = True


class Comment(models.Model, WithLike):
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

    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        abstract = True


class PhotoComment(Comment):
    photo = models.ForeignKey(Photo)


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
        abstract = True


class PhotoLike(Like):
    photo = models.ForeignKey(Photo)


class CommentLike(Like):
    comment = models.ForeignKey(Comment)


class BaseEvent(models.Model, WithComment, WithLike, WithContentType):
    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'
        abstract = True


class Meeting(BaseEvent):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)

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


class Birthday(BaseEvent):
    when = models.DateTimeField(
        u'Когда',
        default=None
    )


class Event(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=1
    )

    name = models.CharField(
        u'Название события',
        max_length=255
    )

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'
