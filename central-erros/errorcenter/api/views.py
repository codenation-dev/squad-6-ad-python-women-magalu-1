from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LogSerializer, OriginSerializer, UserSerializer
from .models import Log, Origin, User

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
