from django.db import models
from pet_profile.models import PetProfiles


class ProcedureTypes(models.Model):
    name = models.CharField(max_length=255, verbose_name='Тип процедуры')

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'

    def __str__(self):
        return self.name


class CalendarRecords(models.Model):
    pet_profile_id = models.ForeignKey(
        PetProfiles,
        on_delete=models.CASCADE,
        verbose_name='Питомец'
    )
    procedure_type_id = models.ForeignKey(
        ProcedureTypes,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Тип процедуры'
    )
    description = models.TextField(
        verbose_name='Описание процедуры',
        blank=True
    )
    procedure_date = models.DateTimeField(
        verbose_name='Дата и время процедуры'
    )
    json_data = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Запись в календаре'
        verbose_name_plural = 'Записи в календаре'

    def __str__(self):
        return self.description
