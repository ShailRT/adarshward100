# Generated by Django 4.2.1 on 2023-06-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_address_profile_bio_alter_profile_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]