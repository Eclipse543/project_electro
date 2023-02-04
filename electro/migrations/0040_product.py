# Generated by Django 4.1.5 on 2023-02-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electro", "0039_remove_products_customer_cart_customer_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="product_files/"),
                ),
                ("url", models.URLField()),
            ],
        ),
    ]