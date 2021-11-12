from django import forms
from captcha.fields import CaptchaField

class Buy_Product(forms.Form):
    first_name = forms.CharField(max_length=100, required=True,label='Your Name')
    last_name = forms.CharField(max_length=100, required=True,label='Surname')
    email = forms.EmailField(required=True,label='email')
    address=forms.CharField(max_length=50,label='Adress')
    postal_code=forms.CharField(max_length=10)
    extra_info = forms.CharField(widget=forms.Textarea(attrs={'cols':40,'rows':3}), max_length=255, required=True,label='Details')
    captcha=CaptchaField(label='What you see?')