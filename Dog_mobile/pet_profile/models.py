from django.db import models
from users.models import CustomUser


class PetTypes(models.Model):
    pet_type = models.CharField(
        max_length=256,
        unique=True,
        verbose_name='Тип питомца',
        blank=False
    )


class PetProfiles(models.Model):
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    pet_name = models.CharField(max_length=255, verbose_name='Имя питомца')
    pet_type_id = models.OneToOneField(
        PetTypes,
        on_delete=models.CASCADE,
        null=False
    )
    age = models.IntegerField(verbose_name='Возраст питомца')
    json_data = models.JSONField()


class MedFiles(models.Model):
    pet_profile_id = models.ForeignKey(PetProfiles, on_delete=models.CASCADE)
    med_file = models.ImageField(
        upload_to='med_files',
        blank=True,
        verbose_name='Файл'
    )
    description = models.TextField(verbose_name='Описание мед.файла')
