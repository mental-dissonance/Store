# Generated by Django 5.0.2 on 2024-04-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_categories_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="categories",
            name="test",
        ),
        migrations.AlterField(
            model_name="categories",
            name="title",
            field=models.TextField(verbose_name="Категория"),
        ),
    ]
