# Generated by Django 5.0.7 on 2024-07-22 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images/')),
                ('title_banner', models.CharField(max_length=20)),
                ('subtitle_banner', models.CharField(max_length=60)),
                ('welcome_video', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='HomeBreakfastImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images/')),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_breakfast_image', to='home.homepage')),
            ],
        ),
        migrations.CreateModel(
            name='HomeRoomImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images/')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_room_image', to='home.homepage')),
            ],
        ),
        migrations.CreateModel(
            name='HomeTourImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images/')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_tour_image', to='home.homepage')),
            ],
        ),
    ]
