from rest_framework import viewsets
from .models import HP, HP1Jutaan, HP2Jutaan
from .serializers import HPSerializer, HP1JutaanSerializer, HP2JutaanSerializer

class HPViewSet(viewsets.ModelViewSet):
    queryset = HP.objects.all()
    serializer_class = HPSerializer

class HP1JutaanViewSet(viewsets.ModelViewSet):
    queryset = HP1Jutaan.objects.all()
    serializer_class = HP1JutaanSerializer

class HP2JutaanViewSet(viewsets.ModelViewSet):
    queryset = HP2Jutaan.objects.all()
    serializer_class = HP2JutaanSerializer
