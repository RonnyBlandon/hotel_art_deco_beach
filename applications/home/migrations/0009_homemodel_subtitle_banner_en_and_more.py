# Generated by Django 5.0.7 on 2024-07-31 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_homemodel_subtitle_banner_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemodel',
            name='subtitle_banner_en',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='homemodel',
            name='title_banner_en',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
