# Generated by Django 4.1.5 on 2023-01-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electro", "0011_topselling_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="newproducts",
            name="discount_percent",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="newproducts",
            name="quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="newproducts",
            name="status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
