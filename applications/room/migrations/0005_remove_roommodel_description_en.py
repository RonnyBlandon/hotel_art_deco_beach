# Generated by Django 5.0.7 on 2024-07-31 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_alter_roommodel_options_roommodel_description_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roommodel',
            name='description_en',
        ),
    ]
