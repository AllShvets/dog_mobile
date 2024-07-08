from django.db import models
from pet_profile.models import PetProfile


class ProcedureType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Тип процедуры'
    )
    key = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Ключ',
        blank=False
    )

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'

    def __str__(self):
        return self.name


class CalendarRecord(models.Model):
    pet_profile = models.ForeignKey(
        PetProfile,
        on_delete=models.CASCADE,
        verbose_name='Питомец'
    )
    procedure_type = models.ForeignKey(
        ProcedureType,
        on_delete=models.CASCADE,
        null=False,
        default=1,
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
