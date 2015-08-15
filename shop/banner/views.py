# coding: utf-8
# author: dlyapun

from django.shortcuts import render
#from django.template import Context
from django.http import HttpResponse
from banner.models import Banner
#from product.models import Product, Categories
#from django.template.loader import get_template

DISABLE = 0
ENABLE = 1
HOT_NEW = 2


def home(request):
    banners = Banner.objects.filter(state=1)
    #new_prods = Product.objects.filter(state=HOT_NEW)[:4] 
    #categories = Categories.objects.all() 
    data = {'banners': banners,
    #'categories':categories,
    #'new_prods': new_prods,
    }
    #banner_template = get_template('home.html')

    #return render(request, banner_template, data)
    #html = banner_template.render(Context(data))
    #return HttpResponse(html)
    return render(request, 'home.html', data)

