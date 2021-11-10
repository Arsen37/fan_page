from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactusForm, UserForm, UserUpdateForm
from django.core.mail import send_mail


def contact_us(request):
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'Contact us', 'name_url': 'contact_us'},
            {'name': 'About us', 'name_url': 'about'},
            ]
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            subject = 'Someone contacted us.'
            content = f"""
            {first_name} {last_name} is trying to contact you.
            Their email address is {email}
            Message: {message}
            """

            send_mail(subject=subject, message=content,
                      from_email='sometestemaill123@gmail.com',
                      recipient_list=['sometestemaill123@gmail.com'])
            return redirect('thank_you')
    else:
        form = ContactusForm()

    return render(request, 'users/contact_us.html', {'form': form, 'title': 'Contact us','menu':menu})


def thank_you(request):
    return render(request, 'users/thank_you.html', {'title': 'Thank You!'})


def register(request):
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'Contact us', 'name_url': 'contact_us'},
            {'name': 'About us', 'name_url': 'about'},
            ]
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('Home')
    else:
        form = UserForm()

    return render(request, 'users/register.html', {'form': form, 'title': 'Register','menu':menu})


@login_required
def profile(request):

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'your account has been updated!')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form, 'title': 'Profile'})
