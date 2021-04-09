
from django.db import models
from datetime import datetime


class User(models.Model):
    """Model definition for User."""
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    GENDER_CHOICES = [
        (MALE, 'male'),
        (FEMALE, 'female'),
        (OTHER, 'other'),
    ]

    # TODO: Define fields here
    user_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(null=True)
    profile_image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=100, null=False, unique=True)
    firebase_uid = models.CharField(
        "firebase User ID", max_length=100, blank=True)
    date_created = models.DateTimeField(default=datetime.now())
    bio = models.TextField(max_length=400)
    isVendor = models.BooleanField(null=True)
    isVerified = models.BooleanField(null=True)
    followers = models.IntegerField(null=True)
    following = models.IntegerField(null=True)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass


class UserFollowerTracker(models.Model):
    follow_id = models.ManyToManyField(
        User, related_name="the_person_being_followed", blank=False)
    follower_id = models.ManyToManyField(
        User, related_name="the_person_doing_the_following", blank=False)
    date_followed = models.DateTimeField(default=datetime.now())

    verbsoe_name_plural = 'UserFollowerTracker'
#
#
#
#
#
#
#
#
#


# adding our profile attributes to our admin
