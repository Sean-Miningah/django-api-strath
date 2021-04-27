from django.urls import include, path
from rest_framework import routers
from .views import ChirpRecordView

router = routers.DefaultRouter()
router.register('', ChirpRecordView)

urlpatterns = [
    path('', include(router.urls)),
]
