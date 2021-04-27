from .models import Chirp
from rest_framework import serializers


class ChirpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chirp
        fields = '__all__'
