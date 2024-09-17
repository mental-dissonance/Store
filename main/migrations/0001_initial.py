# Generated by Django 5.0.2 on 2024-04-29 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("title", models.CharField(max_length=255, verbose_name="Категория")),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Columns",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Колонка",
                "verbose_name_plural": "Колонки",
            },
        ),
        migrations.CreateModel(
            name="Computers",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Компьютер",
                "verbose_name_plural": "Компьютеры",
            },
        ),
        migrations.CreateModel(
            name="Notebooks",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Ноутбук",
                "verbose_name_plural": "Ноутбуки",
            },
        ),
        migrations.CreateModel(
            name="Phones",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Телефон",
                "verbose_name_plural": "Телефоны",
            },
        ),
        migrations.CreateModel(
            name="Tablets",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Планшет",
                "verbose_name_plural": "Планшеты",
            },
        ),
        migrations.CreateModel(
            name="Tvs",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
            ],
            options={
                "verbose_name": "Телевизор",
                "verbose_name_plural": "Телевизоры",
            },
        ),
        migrations.CreateModel(
            name="Products",
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
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("price", models.IntegerField(verbose_name="Цена")),
                ("logo", models.ImageField(upload_to="img/")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.categories",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
    ]
