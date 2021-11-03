from django.urls import path
from .views import main_page, show_post, show_category

urlpatterns = [
    path('', main_page, name='Home'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', show_category, name='category'),
]
