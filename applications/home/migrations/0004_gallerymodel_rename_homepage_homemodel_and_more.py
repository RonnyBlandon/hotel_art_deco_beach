# Generated by Django 5.0.7 on 2024-07-23 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_introductionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='HomePage',
            new_name='HomeModel',
        ),
        migrations.RenameModel(
            old_name='IntroductionPage',
            new_name='IntroductionModel',
        ),
    ]
