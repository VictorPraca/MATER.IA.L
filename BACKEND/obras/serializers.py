from rest_framework import serializers
from .models import Engenheiro

class EngenheiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engenheiro
        fields = '__all__'