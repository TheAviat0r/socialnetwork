# -*- coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db import models


# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password=None):
        if not email:
            raise ValueError(u'Email непременно должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, firstname, lastname):
        user = self.create_user(email, password, firstname, lastname)
        user.is_admin = True
        user.save(using=self._db)
        return user


def upload_imgs(obj, filename):
    to = obj.user.email + "/" + "avatar" + "/" + filename
    return to


class ExtUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        u'Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        u'Аватар',
        blank=True,
        null=True,
        upload_to=upload_imgs
    )
    firstname = models.CharField(
        u'Имя',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        u'Фамилия',
        max_length=40,
        null=True,
        blank=True
    )
    register_date = models.DateField(
        u'Дата регистрации',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Активен',
        default=True
    )
    is_admin = models.BooleanField(
        'Суперпользователь',
        default=False
    )

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.email

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = UserManager()

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
