# Generated by Django 4.0.4 on 2022-06-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0019_alter_image_options_alter_image_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='image_commented_on',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='instagram.image'),
        ),
    ]
