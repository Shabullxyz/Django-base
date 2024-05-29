from django.shortcuts import render
from rest_framework import viewsets
from .models import TablaScrap
from .serializers import TablaScrapSerializer

class TablaScrapViewSet(viewsets.ModelViewSet):
    queryset = TablaScrap.objects.all()
    serializer_class = TablaScrapSerializer

# Create your views here.
