# Generated by Django 4.2.11 on 2024-04-20 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0002_userprofile_post_like_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "follower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follower",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follows",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="like",
            name="post",
        ),
        migrations.RemoveField(
            model_name="like",
            name="user",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="follows",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.AddField(
            model_name="post",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="like", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Like",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
