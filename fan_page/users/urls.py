from django.urls import path
from .views import *

urlpatterns = [
    path('contactus/', contact_us, name='contact_us'),
    path('thankyou/', thank_you, name='thank_you'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]