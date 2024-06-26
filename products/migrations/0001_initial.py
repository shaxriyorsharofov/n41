# Generated by Django 5.0.6 on 2024-05-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("isbn", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="media/default_book_img.png",
                        null=True,
                        upload_to="images/",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("updated_date", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "books",
            },
        ),
    ]
