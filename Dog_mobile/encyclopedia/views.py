from django.shortcuts import render
from rest_framework import generics
from .models import EncyclopediaRecords
from .serializers import EncyclopediaSerializer


class EncyclopediaApiView(generics.ListAPIView):
    queryset = EncyclopediaRecords.objects.all()
    serializer_class = EncyclopediaSerializer
