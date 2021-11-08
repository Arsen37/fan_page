from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .utils import DataMixin
from .models import *


class Main_page(DataMixin, ListView):
    model = Post
    template_name = 'news/intro.html'
    context_object_name = 'post'
    ordering = ['creation_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='F.C.B')
        return dict(list(context.items()) + list(mix_context.items()))


class Show_post(DataMixin, DetailView):
    model = Post
    template_name = 'news/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_con = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(mix_con.items()))


class Show_category(DataMixin, ListView):
    model = Post
    template_name = 'news/intro.html'
    allow_empty = False
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['category_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title=context['post'][0].cat)
        return dict(list(context.items()) + list(mix_context.items()))


class About(DataMixin, TemplateView):
    template_name = 'news/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='About Us')
        return dict(list(context.items()) + list(mix_context.items()))
