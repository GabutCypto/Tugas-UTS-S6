from rest_framework import viewsets
from .models import Kategori, HP, Penjualan
from .serializers import KategoriSerializer, HPSerializer, PenjualanSerializer

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class HPViewSet(viewsets.ModelViewSet):
    queryset = HP.objects.all()
    serializer_class = HPSerializer

class PenjualanViewSet(viewsets.ModelViewSet):
    queryset = Penjualan.objects.all()
    serializer_class = PenjualanSerializer
