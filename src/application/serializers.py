from rest_framework import serializers
from extuser.models import ExtUser

from useractivities.models import Event


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExtUser
        fields = ('firstname', 'lastname', 'email', 'is_staff')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('creator', 'name', 'content_type')
