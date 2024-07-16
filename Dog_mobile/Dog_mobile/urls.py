from django.contrib import admin
from django.urls import path, include, re_path
from encyclopedia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/encyclopedia_list', views.EncyclopediaApiView.as_view()),
    path('pet-profile/', include('pet_profile.urls')),
    path('pet-calendar/', include('pet_calendar.urls')),
]
