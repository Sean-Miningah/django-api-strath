from rest_framework import serializers

# from django.contrib.auth.models import User
# from .models import UserProfile


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['id', 'password',
#                   'username', 'email', 'is_active', ]


# class UserProfileSerializer(serializers.ModelSerializer):
#     """User Serializer to return User Informations"""
#     user = UserSerializer()
#     profile_pic = serializers.ImageField(source="profile_image")

#     class Meta:
#         model = UserProfile
#         fields = ["id", "phonenumber", "country",
#                   "profile_pic", "user", ]
from .models import User, UserFollowerTracker
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
