# Generated by Django 4.1.5 on 2023-01-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("electro", "0002_newproducts"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="newproducts",
            options={"verbose_name_plural": "NewProducts"},
        ),
    ]
