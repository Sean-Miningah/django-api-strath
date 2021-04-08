from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Some additional attributes
    phonenumber = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=100, blank=True)
    firebase_uid = models.CharField(max_length=100, default='', blank=True)


#
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
