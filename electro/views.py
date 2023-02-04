from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Sum
from electro.models import Category, Products, Collection, Order, Cart
from .forms import CustomerRegistrationForm
from django.views import View
from django.contrib.auth.models import User



def index(request):
    contact_list = Products.objects.filter(item_type='np')
    paginator = Paginator(contact_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        "collections": Collection.objects.all(),
        "product": page_obj
    }
    return render(request, "electro/index.html", data)


def category(request, cat_slug):
    cat = Category.objects.get(cat_slug=cat_slug)
    products_ts = Products.objects.filter(category=cat, item_type='ts')
    products_np = Products.objects.filter(category=cat, item_type='np')
    products_tp = Products.objects.filter(category=cat, item_type='tp')
    context = {
        'products_ts': products_ts,
        'products_np': products_np,
        'products_tp': products_tp,
    }
    return render(request, 'electro/product/category.html', context)


def product(request, slug):
    contact_list = Products.objects.filter(item_type='tp')
    paginator = Paginator(contact_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        "details": Products.objects.get(slug=slug),
        "relatedproduct": page_obj,
    }
    return render(request, "electro/product/product.html", data)


def shop(request):
    contact_list = Products.objects.all()
    paginator = Paginator(contact_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        "prod": page_obj,
    }
    return render(request, "electro/store.html", data)


def myaccount(request):
    return render(request, "electro/myaccount.html")


def register(request):
    return render(request, "electro/register.html")


def data_pass(request):
    total_qty1 = Order.objects.aggregate(total_qty=Sum('qty'))['total_qty']
    total_qty = Cart.objects.aggregate(total_qty=Sum('qty'))['total_qty']
    data = {
        "categories": Category.objects.all(),
        "products": Products.objects.all(),
        "newproducts": Products.objects.filter(item_type='np'),
        "topselling": Products.objects.filter(item_type='ts'),
        "trendingproduct": Products.objects.filter(item_type='tp'),
        "cart_details": Cart.objects.all(),
        'total_qty1': total_qty1,
        'total_qty': total_qty,


    }
    return data


def about(request):
    return render(request, "electro/about.html")


def contact(request):
    return render(request, "electro/contact.html")


def add_to_cart(request, slug):
    np = Products.objects.get(slug=slug)
    cart_product = Cart.objects.create(np=np)
    cart_product.save()
    messages.success(request, 'Successfully added to cart')
    data = {"cart_details": Cart.objects.order_by("-id")}
    return render(request, "electro/cart/cart.html", data)


def cart(request):
    cart_items = Cart.objects.all()
    total_qty = Cart.objects.aggregate(total_qty=Sum('qty'))['total_qty']
    data = {
        "cart_details": Cart.objects.order_by("-id"),
        'cart_items': cart_items,
        'total_qty': total_qty,
    }
    return render(request, "electro/cart/cart.html", data)


def add_to_order(request, slug):
    np = Products.objects.get(slug=slug)
    order_product = Order.objects.create(np=np)
    order_product.save()
    messages.success(request, 'Successfully added to order, please proceed to checkout')
    # back = request.META['HTTP_REFERER']
    # return redirect(back)
    data = {
        "order_details": Order.objects.order_by("-id")
    }
    return render(request, 'electro/cart/order.html', data)


def cart_to_order(request, slug):
    np = Products.objects.get(slug=slug)
    order_product = Order.objects.create(np=np)
    order_product.save()
    messages.success(request, 'Successfully added to order, please proceed to checkout')
    cart_product = Cart.objects.get(np=np)
    if cart_product:
        cart_product.delete()
    data = {
        "order_details": Order.objects.order_by("-id")
    }
    return render(request, 'electro/cart/order.html', data)


def order(request):
    order_items = Order.objects.all()
    total_qty1 = Order.objects.aggregate(total_qty=Sum('qty'))['total_qty']
    data = {
        "order_details": Order.objects.order_by("-id"),
        'order_items': order_items,
        'total_qty1': total_qty1,
    }
    return render(request, 'electro/cart/order.html', data)


def checkout(request):
    address = User.objects.all()
    order_items = Order.objects.all()
    shipping_amount = 65
    totalamount = sum(item.qty * item.np.price for item in order_items) + shipping_amount
    return render(request, "electro/checkout.html", {'address':address, 'order_items':order_items, 'totalamount': totalamount})


def remove(request, slug):
    np = Products.objects.get(slug=slug)
    cart_product = Cart.objects.filter(np=np)
    for cart_product in cart_product:
        cart_product.delete()
    back = request.META['HTTP_REFERER']
    messages.success(request, 'Successfully removed from cart')
    return redirect(back)


def cancel(request, slug):
    np = Products.objects.get(slug=slug)
    order_products = Order.objects.filter(np=np)
    for order_product in order_products:
        order_product.delete()
    back = request.META['HTTP_REFERER']
    messages.success(request, 'Your order has been cancelled')
    return redirect(back)


def register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


import os
import stripe
from django.conf import settings 
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse


stripe.api_key = settings.STRIPE_SECRET_KEY


YOUR_DOMAIN = 'http://127.0.0.1:8000/'

def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

def create_checkout_session(request, pk):
    try:
        order = Order.objects.get(id=pk)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        "currency": "usd",
                        "unit_amount": int(order.np.price)*100,
                        "product_data":{
                            "name": order.np.title,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/cancel/',
        )
    except Exception as e:
        return HttpResponse(str(e))

    return HttpResponseRedirect(checkout_session.url)
