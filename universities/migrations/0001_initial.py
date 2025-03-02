# Generated by Django 5.1.6 on 2025-03-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Facultate",
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
                ("nume", models.CharField(max_length=255)),
                ("descriere", models.TextField()),
                (
                    "rating",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
                ),
                (
                    "oameni_pe_loc",
                    models.DecimalField(decimal_places=1, default=0.0, max_digits=3),
                ),
                ("locatie", models.CharField(max_length=255)),
            ],
        ),
    ]
