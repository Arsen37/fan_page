from django.shortcuts import render
from .models import *


def shop_page(request):
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'Contact us', 'name_url': 'contact_us'},
            {'name': 'About us', 'name_url': 'about'},
            {'name': 'Log In', 'name_url': 'login'}, ]

    return render(request, 'shop/shop_page.html', {'menu': menu, 'title': 'Shop'})

