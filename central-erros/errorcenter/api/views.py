from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LogSerializer, OriginSerializer, LevelSerializer
from .models import Log, Origin, Level

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class LevelApiViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
