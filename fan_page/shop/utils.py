from .models import *

category = Category.objects.all()

menu = [{'name': 'News', 'name_url': 'Home'},
        {'name': 'Shop', 'name_url': 'shop'},
        {'name': 'Contact us', 'name_url': 'contact_us'},
        {'name': 'About us', 'name_url': 'about'},
        ]


class ShopMixin:
    paginate_by = 9

    def get_users_context(self, **kwargs):
        context = kwargs
        context['category'] = category
        context['menu'] = menu
        return context
