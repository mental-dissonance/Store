# Generated by Django 5.0.2 on 2024-05-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_delete_columns_delete_computers_delete_notebooks_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="brand",
            field=models.CharField(
                default="Не выбрано", max_length=255, verbose_name="Бренд"
            ),
        ),
    ]
