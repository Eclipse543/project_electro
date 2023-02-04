from django.urls import path
from . import views




urlpatterns = [
    path("", views.index, name="index"),
    path("category/<cat_slug>", views.category, name="category"),
    path("product/<slug>", views.product, name="product"),
    path("shop/", views.shop, name="shop"),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("add_to_cart/<slug>", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("add_to_order/<slug>", views.add_to_order, name="add_to_order"),
    path("cart_to_order/<slug>", views.cart_to_order, name="cart_to_order"),
    path("order/", views.order, name="order"),
    path("remove/<slug>", views.remove, name="remove"),
    path("cancel/<slug>", views.cancel, name="cancel"),
    path('register/', views.register, name='register'),


]
