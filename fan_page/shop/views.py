from django.shortcuts import render
from .models import *
from django.shortcuts import render


def shop_page(request):
    menu = {
        'News': 'News',
        'Shop': 'Shop',
        'Contact us': 'Contact us',
        'About us': 'About us',
        'Log In': 'Log In'
    }
    return render(request, 'shop/shop_page.html', {'menu': menu, 'title': 'Shop'})

