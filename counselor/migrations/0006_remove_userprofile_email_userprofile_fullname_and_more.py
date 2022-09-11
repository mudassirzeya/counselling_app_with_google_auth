# Generated by Django 4.1.1 on 2022-09-08 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("counselor", "0005_userprofile_user_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="email",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="fullname",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name="StudentExtendedProfile",
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
                    "prepared_from",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("rank", models.CharField(blank=True, max_length=100, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("date_of_joining", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="counselor.userprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CounsellorExtendedProfile",
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
                ("college", models.CharField(blank=True, max_length=100, null=True)),
                ("from_yr", models.CharField(blank=True, max_length=100, null=True)),
                ("to_yr", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "current_job",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("counselling_thought", models.TextField(blank=True, null=True)),
                ("date_of_joining", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="counselor.userprofile",
                    ),
                ),
            ],
        ),
    ]
