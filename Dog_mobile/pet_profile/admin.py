from django.contrib import admin
from .models import PetTypes, PetProfiles, MedFiles

admin.site.register(PetTypes)
admin.site.register(PetProfiles)
admin.site.register(MedFiles)
