# Generated by Django 4.2.6 on 2023-12-14 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("breeds", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BreedType",
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
                ("breed_type", models.CharField(default=None, max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name="breed",
            name="breed_type",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="breeds.breedtype",
            ),
        ),
    ]
