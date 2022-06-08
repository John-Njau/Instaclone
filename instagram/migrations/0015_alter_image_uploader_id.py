# Generated by Django 4.0.4 on 2022-06-07 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0014_remove_image_uploader_image_uploader_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='uploader_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploader', to=settings.AUTH_USER_MODEL),
        ),
    ]
