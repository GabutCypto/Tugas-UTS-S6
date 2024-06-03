from rest_framework import serializers
from .models import Kategori, HP, Penjualan

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class HPSerializer(serializers.ModelSerializer):
    kategori = serializers.PrimaryKeyRelatedField(queryset=Kategori.objects.all())

    class Meta:
        model = HP
        fields = '__all__'

class PenjualanSerializer(serializers.ModelSerializer):
    hp = serializers.PrimaryKeyRelatedField(queryset=HP.objects.all())

    class Meta:
        model = Penjualan
        fields = '__all__'
