from rest_framework import serializers
from pet_profile.models import PetProfile, MedFile


class PetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetProfile
        fields = '__all__'


class MedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedFile
        fields = '__all__'
