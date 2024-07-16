from django.urls import path
from pet_profile.views import (
    PetProfileCreateView,
    PetProfileUpdateView,
    MedFileCreateView,
    MedFileUpdateView
)


app_name = 'pet_profile'

urlpatterns = [
    path(
        'create/',
        PetProfileCreateView.as_view(),
        name='pet-profile-create'
    ),
    path(
        'update/<int:pk>/',
        PetProfileUpdateView.as_view(),
        name='pet-profile-update'
    ),
    path(
        'medfile-create/',
        MedFileCreateView.as_view(),
        name='med-file-create'
    ),
    path(
        'medfile-update/<int:pk>/',
        MedFileUpdateView.as_view(),
        name='med-file-update'
    ),
]
