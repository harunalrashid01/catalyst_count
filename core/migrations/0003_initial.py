# Generated by Django 5.0.6 on 2024-06-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0002_delete_company"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255)),
                ("domain", models.CharField(max_length=255)),
                ("year_founded", models.IntegerField()),
                ("industry", models.CharField(max_length=100)),
                ("size_range", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("linkedin_url", models.URLField()),
                ("current_employee_estimate", models.IntegerField()),
                ("total_employee_estimate", models.IntegerField()),
            ],
        ),
    ]
