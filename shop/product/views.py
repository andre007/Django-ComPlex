# coding=utf-8

from django.shortcuts import render, render_to_response
from product.models import Product, Categories
from cart import Cart
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse



def product_list(request, id):
    categories = Categories.objects.all()
    products = Product.objects.filter(category__id=id)
    data = {'categories': categories, 'products': products}
    return render(request, 'product_list.html', data)
    #return render_to_response('product_list.html', data)
    #prodlist_template = get_template('product_list.html')

    
    #html = prodlist_template.render(Context(data))
    #return HttpResponse(html)



def product_detail(request, id):
    categories = Categories.objects.all()
    product = Product.objects.get(id=id)
    data = {'product': product, 'categories': categories}
    return render(request, 'product_detail.html', data)

def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    #data = {'product': product}
    cart.add(product, product.price, quantity)
    return request

def remove_from_cart(request, product_id):
    print("Delete function starts")
    product = Product.objects.get(id=product_id)
    print(product)
    cart = Cart(request)
    cart.remove(product)

def get_cart(request):
    return render(request, 'cart.html', dict(cart=Cart(request)))