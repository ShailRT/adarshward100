# Generated by Django 4.2.1 on 2023-06-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_on_home_slide_gallery_on_home_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_created',
            field=models.DateTimeField(),
        ),
    ]
