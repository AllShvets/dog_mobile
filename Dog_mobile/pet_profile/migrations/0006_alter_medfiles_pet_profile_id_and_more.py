# Generated by Django 5.0.6 on 2024-06-27 21:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_profile', '0005_alter_medfiles_options_alter_petprofiles_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='medfiles',
            name='pet_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_profile.petprofiles', verbose_name='Питомец'),
        ),
        migrations.AlterField(
            model_name='petprofiles',
            name='pet_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_profile.pettypes', verbose_name='Тип процедуры'),
        ),
        migrations.AlterField(
            model_name='petprofiles',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
