from django.shortcuts import render
from rest_framework import generics
from pet_profile.models import PetProfile, MedFile
from pet_profile.serializers import PetProfileSerializer, MedFileSerializer


class PetProfileCreateView(generics.CreateAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer


class PetProfileUpdateView(generics.UpdateAPIView):
    queryset = PetProfile.objects.all()
    serializer_class = PetProfileSerializer


class MedFileCreateView(generics.CreateAPIView):
    queryset = MedFile.objects.all()
    serializer_class = MedFileSerializer


class MedFileUpdateView(generics.CreateAPIView):
    queryset = MedFile.objects.all()
    serializer_class = MedFileSerializer
