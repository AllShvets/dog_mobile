from rest_framework import serializers
from pet_calendar.models import CalendarRecord


class CalendarRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarRecord
        fields = '__all__'
