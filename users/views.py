# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User

# from .serializers import *
# from .models import *


# class UserRecordView(viewsets.ModelViewSet):
#     serializer_class = UserProfileSerializer

#     def get_queryset(self):
#         users = UserProfile.objects.all()
#         return users

#     def create(self, request, *args, **kwargs):
#         user_data = request.data

#         new_user = User.objects.create(password=user_data["user"]["password"],
#                                        username=user_data["user"]["username"], email=user_data["user"]["email"],
#                                        is_active=user_data["user"]["is_active"])
#         new_user.save()
#         new_userprofile = UserProfile.objects.create(user=new_user, phonenumber=user_data["phonenumber"],
#                                                      country=user_data["country"], profile_image=user_data["profile_image"])
#         new_userprofile.save()

#         serializer = UserProfileSerializer(new_userprofile)

#         return Response(serializer)
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User


class UserRecordView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_created')
    serializer_class = UserSerializer
