# Generated by Django 5.0.6 on 2024-06-27 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='encyclopediarecords',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
