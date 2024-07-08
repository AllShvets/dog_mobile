from django.db import models
from users.models import CustomUser


class PetType(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Тип питомца',
        blank=False
    )
    key = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Ключ',
        blank=False
    )

    class Meta:
        verbose_name = 'Тип питомца'
        verbose_name_plural = 'Тип питомца'

    def __str__(self):
        return self.pet_type


class PetProfile(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    pet_name = models.CharField(max_length=255, verbose_name='Имя питомца')
    pet_type = models.ForeignKey(
        PetType,
        on_delete=models.CASCADE,
        null=False,
        default=1,
        verbose_name='Тип процедуры'
    )
    age = models.IntegerField(verbose_name='Возраст питомца')
    json_data = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = 'Профиль питомца'
        verbose_name_plural = 'Профили питомцев'

    def __str__(self):
        return self.pet_name


class MedFile(models.Model):
    pet_profile = models.ForeignKey(
        PetProfile,
        on_delete=models.CASCADE,
        default=1,
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
