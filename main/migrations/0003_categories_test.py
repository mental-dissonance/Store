# Generated by Django 5.0.2 on 2024-04-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_categories_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="categories",
            name="test",
            field=models.CharField(
                default="hui", max_length=255, verbose_name="Проверка"
            ),
        ),
    ]
