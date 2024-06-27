from django.db import models
from users.models import CustomUser


class PetTypes(models.Model):
    pet_type = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Тип питомца',
        blank=False
    )

    class Meta:
        verbose_name = 'Тип питомца'
        verbose_name_plural = 'Тип питомца'

    def __str__(self):
        return self.pet_type


class PetProfiles(models.Model):
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    pet_name = models.CharField(max_length=255, verbose_name='Имя питомца')
    pet_type_id = models.ForeignKey(
        PetTypes,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='Тип процедуры'
    )
    age = models.IntegerField(verbose_name='Возраст питомца')
    json_data = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Профиль питомца'
        verbose_name_plural = 'Профили питомцев'

    def __str__(self):
        return self.pet_name


class MedFiles(models.Model):
    pet_profile_id = models.ForeignKey(
        PetProfiles,
        on_delete=models.CASCADE,
        verbose_name='Питомец'
    )
    med_file = models.ImageField(
        upload_to='med_files',
        blank=True,
        verbose_name='Файл'
    )
    description = models.TextField(verbose_name='Описание мед.файла')

    class Meta:
        verbose_name = 'Мед.файл'
        verbose_name_plural = 'Мед.файлы'

    def __str__(self):
        return self.description
