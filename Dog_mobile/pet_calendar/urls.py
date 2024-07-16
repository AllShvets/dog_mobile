from django.urls import path
from pet_calendar.views import (
    CalendarRecordCreateView,
    CalendarRecordUpdateView
)

app_name = 'pet_calendar'

urlpatterns = [
    path(
        'create/',
        CalendarRecordCreateView.as_view(),
        name='pet-calendar-create'
    ),
    path(
        'update/<int:pk>/',
        CalendarRecordUpdateView.as_view(),
        name='pet-calendar-update'
    ),
]
