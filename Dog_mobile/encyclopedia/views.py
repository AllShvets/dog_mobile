from django.shortcuts import render
from rest_framework import generics
from .models import EncyclopediaRecord
from .serializers import EncyclopediaSerializer


class EncyclopediaApiView(generics.ListAPIView):
    queryset = EncyclopediaRecord.objects.all()
    serializer_class = EncyclopediaSerializer
    http_method_names = ['get']
