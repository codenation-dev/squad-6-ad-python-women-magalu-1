from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LogSerializer, OriginSerializer
from .models import Log, Origin

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

