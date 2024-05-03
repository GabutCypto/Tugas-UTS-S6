from rest_framework import serializers
from .models import HP, HP1Jutaan, HP2Jutaan

class HPSerializer(serializers.ModelSerializer):
    class Meta:
        model = HP
        fields = '__all__'

class HP1JutaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HP1Jutaan
        fields = '__all__'

class HP2JutaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HP2Jutaan
        fields = '__all__'
