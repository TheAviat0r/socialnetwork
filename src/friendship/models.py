from __future__ import unicode_literals

from django.db import models
from extuser.models import ExtUser

class Relations(models.Model):
	ACCEPTED = 'acc'
	DECLINED = 'decl'
	
	FRIENDSHIP_STATES = (
		(ACCEPTED, 'accepted'),
		(DECLINED, 'declined'),
	)

	sender = models.ForeignKey(ExtUser, related_name='sender+')
	receiver = models.ForeignKey(ExtUser, related_name='receiver+')

	sender_state = models.CharField(max_length=10, choices=FRIENDSHIP_STATES)
	receiver_state = models.CharField(max_length=10, choices=FRIENDSHIP_STATES)



# Create your models here.
