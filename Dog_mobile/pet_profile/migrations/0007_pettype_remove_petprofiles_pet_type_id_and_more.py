# Generated by Django 5.0.6 on 2024-07-08 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_calendar', '0006_calendarrecord_proceduretype_and_more'),
        ('pet_profile', '0006_alter_medfiles_pet_profile_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Тип питомца')),
                ('key', models.CharField(max_length=50, unique=True, verbose_name='Ключ')),
            ],
            options={
                'verbose_name': 'Тип питомца',
                'verbose_name_plural': 'Тип питомца',
            },
        ),
        migrations.RemoveField(
            model_name='petprofiles',
            name='pet_type_id',
        ),
        migrations.RemoveField(
            model_name='petprofiles',
            name='user_id',
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=255, verbose_name='Имя питомца')),
                ('age', models.IntegerField(verbose_name='Возраст питомца')),
                ('json_data', models.JSONField(blank=True, default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('pet_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pet_profile.pettype', verbose_name='Тип процедуры')),
            ],
            options={
                'verbose_name': 'Профиль питомца',
                'verbose_name_plural': 'Профили питомцев',
            },
        ),
        migrations.CreateModel(
            name='MedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_file', models.ImageField(blank=True, upload_to='med_files', verbose_name='Файл')),
                ('description', models.TextField(verbose_name='Описание мед.файла')),
                ('pet_profile', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pet_profile.petprofile', verbose_name='Питомец')),
            ],
            options={
                'verbose_name': 'Мед.файл',
                'verbose_name_plural': 'Мед.файлы',
            },
        ),
        migrations.DeleteModel(
            name='MedFiles',
        ),
        migrations.DeleteModel(
            name='PetTypes',
        ),
        migrations.DeleteModel(
            name='PetProfiles',
        ),
    ]