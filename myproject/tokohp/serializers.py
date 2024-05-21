from rest_framework import serializers
from .models import Kategori, HP, Penjualan

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class HPSerializer(serializers.ModelSerializer):
    kategori = KategoriSerializer()

    class Meta:
        model = HP
        fields = '__all__'

class PenjualanSerializer(serializers.ModelSerializer):
    hp = HPSerializer()

    class Meta:
        model = Penjualan
        fields = '__all__'
