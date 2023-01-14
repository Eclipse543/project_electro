from django.contrib import admin
from .models import Category, Products, Collection, Cart, Order, Customer


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


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
    list_display = ("id", "np", "qty", "color")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("np", "qty", "order_date")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "address", "city", "locality")
