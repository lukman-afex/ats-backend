# Generated by Django 4.0.6 on 2022-08-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_author_profile_image_alter_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
