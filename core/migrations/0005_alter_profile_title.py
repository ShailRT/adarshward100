# Generated by Django 4.2.1 on 2023-06-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Media Prabhari', 'media prabhari'), ('Counselor', 'counselor'), ('Citizen', 'citizen'), ('Mayor', 'mayor')], default='citizen', max_length=120),
        ),
    ]
