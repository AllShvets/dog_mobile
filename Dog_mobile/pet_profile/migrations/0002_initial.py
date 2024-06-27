# Generated by Django 5.0.6 on 2024-06-27 19:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet_profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='petprofiles',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='medfiles',
            name='pet_profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pet_profile.petprofiles'),
        ),
        migrations.AddField(
            model_name='petprofiles',
            name='pet_type_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pet_profile.pettypes'),
        ),
    ]