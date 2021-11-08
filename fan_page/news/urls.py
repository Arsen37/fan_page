from django.urls import path
from .views import *
urlpatterns = [
    path('', Main_page.as_view(), name='Home'),
    path('post/<slug:post_slug>/', Show_post.as_view(), name='post'),
    path('category/<slug:category_slug>/', Show_category.as_view(), name='category'),
    path('about/',About.as_view(),name='about'),
]
