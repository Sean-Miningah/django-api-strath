from django.db import models
from datetime import datetime

from users.models import User
from Channels.models import Channel

# Create your models here.


class Chirp(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(
        Channel, null=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=datetime.now())
    chirp_image = models.ImageField(blank=True, upload_to='chirp_pics')
    chirp_video = models.FileField(blank=True, upload_to='videos/%Y/%m/%d/')
    chirp_content = models.TextField(max_length=400)
    last_modified = models.DateTimeField(default=datetime.now())


class ChirpImage(models.Model):
    main_image = models.ImageField(
        blank=True, upload_to="chirpimage/%Y/%m/%d /")
    image_two = models.ImageField(
        blank=True, upload_to="chirpimage/%Y/%m/%d /")
    chirp_id = models.ForeignKey(Chirp, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ChirpImages'


class ChirpPoll(models.Model):
    poll_title = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(default=datetime.now())
    agree_count = models.IntegerField(default=0)
    disagree_count = models.IntegerField(default=0)
    chirp_id = models.ForeignKey(Chirp, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ChirpPolls'
