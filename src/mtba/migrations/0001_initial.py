# Generated by Django 4.0.6 on 2022-07-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DirectionDestination",
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
                ("name", models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Stops",
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
                ("stop_id", models.CharField(max_length=100, null=True)),
                ("platform_name", models.CharField(max_length=100, null=True)),
                ("description", models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Routes",
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
                ("name", models.CharField(default=None, max_length=100)),
                ("route_id", models.CharField(default=None, max_length=100)),
                ("fare_class", models.CharField(default=None, max_length=100)),
                (
                    "direction_destinations",
                    models.ManyToManyField(null=True, to="mtba.directiondestination"),
                ),
            ],
        ),
    ]
