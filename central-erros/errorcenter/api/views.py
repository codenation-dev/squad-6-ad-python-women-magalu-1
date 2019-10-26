from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Log, Origin, User, Environment, Level
from .serializers import (LogSerializer, 
                          OriginSerializer, 
                          UserSerializer, 
                          EnvironmentSerializer,
                          LevelSerializer)

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class LevelApiViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnvironmentListOnlyApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
