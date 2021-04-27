from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import ChirpSerializer
from .models import Chirp


class ChirpRecordView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Chirp.objects.all().order_by('-date_created')
    serializer_class = ChirpSerializer
