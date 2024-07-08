from rest_framework import serializers
from .models import EncyclopediaRecord


class EncyclopediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncyclopediaRecord
        fields = ('title', 'description')
