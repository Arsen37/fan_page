from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactusForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=500, required=True)


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']