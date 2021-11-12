from django.urls import path
from .views import *

urlpatterns = [
    path('shop/',Shop_attributes.as_view(), name='shop'),
    path('product/<slug:product_slug>/',Product_detail.as_view(),name='product' ),
    path('cat/<slug:cat_slug>/',Product_category.as_view(),name='cat'),
    path('buy/<slug:buy_slug>',product_buy,name='order'),
    path('thanks/',Thanks.as_view(),name='thanks')
]