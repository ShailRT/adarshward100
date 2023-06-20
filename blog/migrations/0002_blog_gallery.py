# Generated by Django 4.2.1 on 2023-06-19 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_name_author_title_remove_author_bio_and_more'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='gallery',
            field=models.ManyToManyField(blank=True, null=True, related_name='blog_gallery', to='core.gallery'),
        ),
    ]
