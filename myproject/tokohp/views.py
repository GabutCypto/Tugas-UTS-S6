from rest_framework import generics
from .models import Kategori, HP, Penjualan
from .serializers import KategoriSerializer, HPSerializer, PenjualanSerializer

class KategoriListCreateView(generics.ListCreateAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class KategoriDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class HPListCreateView(generics.ListCreateAPIView):
    queryset = HP.objects.all()
    serializer_class = HPSerializer

class HPDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HP.objects.all()
    serializer_class = HPSerializer

class PenjualanListCreateView(generics.ListCreateAPIView):
    queryset = Penjualan.objects.all()
    serializer_class = PenjualanSerializer

class PenjualanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Penjualan.objects.all()
    serializer_class = PenjualanSerializer
