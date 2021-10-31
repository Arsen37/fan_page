from . import views as news_views
from django.urls import path, include

urlpatterns = [
    path('home/', news_views.home, name='home')
]
