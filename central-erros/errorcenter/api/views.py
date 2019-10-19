from django.shortcuts import render

from rest_framework import viewsets
from .serializers import OriginSerializer
from .models  import Origin

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer