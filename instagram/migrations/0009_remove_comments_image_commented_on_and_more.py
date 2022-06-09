# Generated by Django 4.0.4 on 2022-06-07 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0008_remove_follow_user_profile_date_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='image_commented_on',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='follow',
            name='following',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='liked_image',
        ),
        migrations.AddField(
            model_name='follow',
            name='user_am_following',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='user_following_me',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='like',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='image_likes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]