# Generated by Django 4.1.5 on 2023-01-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electro", "0007_topselling"),
    ]

    operations = [
        migrations.AddField(
            model_name="newproducts",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="newproducts",
            name="old_price",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="topselling",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
