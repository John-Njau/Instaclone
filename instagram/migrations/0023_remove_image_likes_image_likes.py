# Generated by Django 4.0.4 on 2022-06-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0022_alter_image_comments_alter_image_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.IntegerField(default=1, verbose_name='Likes'),
            preserve_default=False,
        ),
    ]