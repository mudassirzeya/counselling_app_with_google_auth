# Generated by Django 4.1.1 on 2022-09-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counselor", "0004_userprofile_google_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="user_status",
            field=models.CharField(
                blank=True,
                choices=[("approved", "approved"), ("unapproved", "unapproved")],
                max_length=100,
            ),
        ),
    ]
