from django.db import models
from pet_profile.models import PetProfiles


class ProcedureTypes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип процедуры')
    description = models.TextField(verbose_name='Описание процедуры')


class CalendarRecords(models.Model):
    pet_profile_id = models.ForeignKey(
        PetProfiles,
        on_delete=models.CASCADE
    )
    procedure_type_id = models.ForeignKey(
        ProcedureTypes,
        on_delete=models.CASCADE,
        null=False,
    )
    procedure_date = models.DateTimeField(
        verbose_name='Дата и время процедуры'
    )
