from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .utils import ShopMixin
from .forms import *
from .models import *


class Shop_attributes(ShopMixin, ListView):
    model = Attributes
    template_name = 'shop/shop_page.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        u_context = self.get_users_context(title='Shop')
        return dict(list(context.items()) + list(u_context.items()))


class Product_detail(ShopMixin, DetailView):
    model = Attributes
    template_name = 'shop/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        u_context = self.get_users_context(title=context['product'])
        return dict(list(context.items()) + list(u_context.items()))


class Product_category(ShopMixin, ListView):
    model = Attributes
    template_name = 'shop/shop_page.html'
    allow_empty = False
    context_object_name = 'products'

    def get_queryset(self):
        return Attributes.objects.filter(category__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coments'] = Category.objects.all()
        mix_context = self.get_users_context(title=context['products'][0].category)
        return dict(list(context.items()) + list(mix_context.items()))


def product_buy(request, buy_slug):
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'Contact us', 'name_url': 'contact_us'},
            {'name': 'About us', 'name_url': 'about'},
            ]
    product = get_object_or_404(Attributes, slug=buy_slug)

    if request.method == 'POST':
        form = Buy_Product(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            extra = form.cleaned_data.get('extra_info')
            address = form.cleaned_data.get('address')
            post_code = form.cleaned_data.get('postal_code')

            subject = 'Order'
            content = f"""
            {first_name} {last_name} want's to buy product.this product {product.title}
            l code'{post_code}'
            Details: {extra} 
            """

            send_mail(subject=subject, message=content,
                      from_email='sometestemaill123@gmail.com',
                      recipient_list=['sometestemaill123@gmail.com'])
            return redirect('thanks')
    else:
            form = Buy_Product()
    title='Order'
    return render(request, 'shop/buying.html', {'form': form, 'menu': menu, 'product': product,'title':title})

class Thanks(ShopMixin,TemplateView):
    template_name = 'shop/thank_s.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        u_context = self.get_users_context()
        return dict(list(context.items()) + list(u_context.items()))
