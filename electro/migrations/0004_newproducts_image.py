# Generated by Django 4.1.5 on 2023-01-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electro", "0003_alter_category_options_alter_newproducts_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="newproducts",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
    ]
