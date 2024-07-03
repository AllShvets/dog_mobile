from rest_framework import serializers
from .models import EncyclopediaRecords


class EncyclopediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncyclopediaRecords
        fields = ('title', 'description')
