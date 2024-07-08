from django.contrib import admin
from .models import PetType, PetProfile, MedFile

admin.site.register(PetType)
admin.site.register(PetProfile)
admin.site.register(MedFile)
