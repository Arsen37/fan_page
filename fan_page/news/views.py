from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import *


def main_page(requset):
    menu = {

        'News': 'News',
        'Shop': 'Shop',
        'Contact us': 'Contact us',
        'About us': 'About us',
        'Log In': 'Log In'
    }
    category = Category.objects.all()
    post = Post.objects.all()

    return render(requset, 'news/intro.html', {'menu': menu, 'category': category, 'post': post,'title':'F.C.B'})


def show_post(request, post_slug):
    menu = {
        'News': 'News',
        'Shop': 'Shop',
        'Contact us': 'Contact us',
        'About us': 'About us',
        'Log In': 'Log In'
    }
    post = get_object_or_404(Post, slug=post_slug)
    category = Category.objects.all()
    return render(request, 'news/post.html', {'menu': menu, 'post': post, 'category': category})


def show_category(requset, category_slug):
    menu = {
        'News': 'News',
        'Shop': 'Shop',
        'Contact us': 'Contact us',
        'About us': 'About us',
        'Log In': 'Log In'
    }
    category = Category.objects.all()
    post = Post.objects.filter(cat__slug=category_slug)
    if len(post) ==0:
        raise Http404
    title='Categories'
    return render(requset, 'news/show_category.html', {'menu': menu, 'category': category, 'post': post,'title':title})
