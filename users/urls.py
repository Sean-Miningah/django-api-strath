from django.urls import path, include
from .models import User
from rest_framework import routers
from .views import UserRecordView


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_name', 'email', 'phone_number', 'country', 'password',
#                   'profile_image']


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'user-register', UserRecordView.as_view(),
#                 basename="userrecord")
router = routers.DefaultRouter()
router.register('users', UserRecordView, basename="wanaotumia")

urlpatterns = [
    path('', include(router.urls))
]
