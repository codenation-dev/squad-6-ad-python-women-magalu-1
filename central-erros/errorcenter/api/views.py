from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import LogSerializer
from .models import Log

class LogApiViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
