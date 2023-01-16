
from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    cat_slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Collection(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to="img/", null=True, blank=True)

    def __str__(self):
        return self.title


class Products(models.Model):
    item_category_field = (
        ('ts', 'topselling'),
        ('np', 'newproducts'),
        ("tp", 'trendingproduct'),
    )
    status_field = (
        ('NEW', 'NEW'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_type = models.CharField(choices=item_category_field, max_length=2, null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    price = models.FloatField()
    old_price = models.FloatField(null=True)
    image = models.ImageField(upload_to="img/", null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    discount_percent = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(choices=status_field, max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)


class Cart(models.Model):
    np = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    color = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.np)


class Order(models.Model):
    np = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.np)
