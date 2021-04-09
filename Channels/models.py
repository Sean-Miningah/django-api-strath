from django.db import models
from datetime import datetime

from users.models import User

# Create your models here.


class Channel(models.Model):
    channel_name = models.CharField(max_length=100, unique=True)
    user_id = models.ForeignKey(User, null=False,  on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=False)
    date_created = models.DateTimeField(default=datetime.now())
    no_of_subscribers = models.IntegerField(default=0)


class ChannelSubscriberTracker(models.Model):
    channel_id = models.ForeignKey(
        Channel, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name_plural = "ChannelSubscriberTrackers"
