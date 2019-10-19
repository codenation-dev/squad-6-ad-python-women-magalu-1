from rest_framework import serializers
from .models import Log

class OriginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origin
        fields = ['description']
        read_only_fields = ['description']