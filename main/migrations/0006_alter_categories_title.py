# Generated by Django 5.0.2 on 2024-04-29 18:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_products_cat"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="title",
            field=models.CharField(max_length=255, verbose_name="Категория"),
        ),
    ]
