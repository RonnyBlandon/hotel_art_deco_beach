# Generated by Django 5.0.7 on 2024-07-31 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_roommodel_description_en'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roommodel',
            name='description_en',
        ),
    ]
