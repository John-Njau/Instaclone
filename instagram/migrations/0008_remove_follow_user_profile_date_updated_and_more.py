# Generated by Django 4.0.4 on 2022-06-07 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0007_delete_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follow',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('liked_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.image')),
            ],
            options={
                'verbose_name_plural': 'likes',
            },
        ),
    ]
