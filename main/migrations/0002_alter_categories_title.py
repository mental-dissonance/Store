# Generated by Django 5.0.2 on 2024-04-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="title",
            field=models.IntegerField(verbose_name="Категория"),
        ),
    ]
