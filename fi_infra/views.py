from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import AtivoSerializer
from .models import Ativo


class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all().order_by('ticker')
    serializer_class = AtivoSerializer