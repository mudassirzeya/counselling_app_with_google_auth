# Generated by Django 4.1.1 on 2022-09-11 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("counselor", "0008_rename_comment_to_comment_comment_to"),
    ]

    operations = [
        migrations.CreateModel(
            name="Frequestly_Asked_Question",
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
                ("question", models.CharField(blank=True, max_length=500, null=True)),
                ("answer", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
