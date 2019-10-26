from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Log, Origin, User, Environment
from .serializers import (LogSerializer, 
                          OriginSerializer, 
                          UserSerializer, 
                          EnvironmentSerializer)

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

class OriginApiViewSet(viewsets.ModelViewSet):
    queryset = Origin.objects.all()
    serializer_class = OriginSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EnvironmentListOnlyApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
