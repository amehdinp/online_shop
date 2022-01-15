from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request, slug=None):
    products = Product.objects.filter(available=True)
    categorys = Category.objects.all()#filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category= category)
    return render(request, 'shop/home.html', {'products': products, 'categorys': categorys})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})


