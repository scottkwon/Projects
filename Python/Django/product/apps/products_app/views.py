# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    Product.objects.create(name='Nike Lunar', description='These are the latest and greatest in Nike Running Technology', weight=2, price=30, cost=220, category='shoes')
    Product.objects.create(name='Adidas Boost', description='These are the latest and greatest in Adidas Running Technology', weight=2, price=30, cost=180, category='shoes')
    Product.objects.create(name='Vans Ultracushion', description='These are the latest and greatest in Vans Skateboarding Technology', weight=2, price=15, cost=60, category='shoes')
    products = product.objects.all()
    for product in products:
        print product.name, product.description, product.weight, product.price, product.cost, product.category
    return render(request, 'products_app/index.html')
