from django.shortcuts import render
from rest_framework import generics
from pet_calendar.models import CalendarRecord
from pet_profile.serializers import CalendarRecordSerializer


class CalendarRecordCreateView(generics.CreateAPIView):
    queryset = CalendarRecord.objects.all()
    serializer_class = CalendarRecordSerializer


class CalendarRecordUpdateView(generics.UpdateAPIView):
    queryset = CalendarRecord.objects.all()
    serializer_class = CalendarRecordSerializer
