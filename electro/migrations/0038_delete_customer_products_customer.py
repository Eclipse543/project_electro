# Generated by Django 4.1.5 on 2023-01-29 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("electro", "0037_rename_slug_category_cat_slug"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.AddField(
            model_name="products",
            name="customer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
