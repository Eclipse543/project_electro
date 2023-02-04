from django.contrib import admin
from .models import Category, Products, Collection, Cart, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "cat_slug")
    prepopulated_fields = {"cat_slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("category", "item_type", "title", "slug", "price", "image", "description", "discount_percent", "status")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "image")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("customer","id", "np", "qty", "color")

""
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","np", "qty", "order_date")


