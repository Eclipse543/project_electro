from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from electro.models import Category, Customer, Products, Collection, Order, Cart


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


def category(request, slug):
    return render(request, 'electro/product/category.html')


def product(request, slug):
    contact_list = Products.objects.filter(item_type='tp')
    paginator = Paginator(contact_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        "details": Products.objects.get(slug=slug),
        "relatedproduct": page_obj

    }
    return render(request, "electro/product/product.html", data)


def shop(request):
    return render(request, "electro/store.html")


def myaccount(request):
    return render(request, "electro/myaccount.html")


def register(request):
    return render(request, "electro/register.html")


def data_pass(request):
    data = {
        "category": Category.objects.all(),
        "newproducts": Products.objects.filter(item_type='np'),
        "topselling": Products.objects.filter(item_type='ts'),
        "trendingproduct": Products.objects.filter(item_type='tp'),
        "cart_details": Cart.objects.all(),

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
    data = {"cart_details": Cart.objects.order_by("-id")}
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
    data = {
        "order_details": Order.objects.order_by("-id")
    }
    return render(request, 'electro/cart/order.html', data)


def checkout(request):
    address = Customer.objects.all()
    order_items = Order.objects.all()
    amount = 0.0
    shipping_amount = 65.0
    order_product = [p for p in Order.objects.all()]
    if order_product:
        for p in order_product:
            calculate = (p.qty * p.np.price)
            amount += calculate
        totalamount = amount + shipping_amount
    return render(request, "electro/checkout.html", {'address': address, 'order_items':order_items, 'totalamount': totalamount})

def remove(request, slug):
    np = Products.objects.get(slug=slug)
    cart_product = Cart.objects.get(np=np)
    if cart_product:
        cart_product.delete()
    back = request.META['HTTP_REFERER']
    messages.success(request, 'Successfully removed from cart')
    return redirect(back)


def cancel(request, slug):
    np = Products.objects.get(slug=slug)
    order_product = Order.objects.get(np=np)
    if order_product:
        order_product.delete()
    back = request.META['HTTP_REFERER']
    messages.success(request, 'Your order has been cancelled')
    return redirect(back)
