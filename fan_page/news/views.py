from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView,CreateView

from .utils import DataMixin
from .models import *
from .forms import *


class Main_page(DataMixin, ListView):
    model = Post
    template_name = 'news/intro.html'
    context_object_name = 'post'
    ordering = ['creation_date']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='F.C.B')
        return dict(list(context.items()) + list(mix_context.items()))


def show_post(request, post_slug):

    post = get_object_or_404(Post, slug=post_slug)
    category = Category.objects.all()
    menu = [{'name': 'News', 'name_url': 'Home'},
            {'name': 'Shop', 'name_url': 'shop'},
            {'name': 'Contact us', 'name_url': 'contact_us'},
            {'name': 'About us', 'name_url': 'about'},
            ]
    comments = Comentaries.objects.filter(post__slug=post_slug)
    if request.method == "POST":
        form = Coments_create(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.post = post
            form.save()
            return redirect(show_post, post_slug)
    else:
        form = Coments_create()

    return render(request, 'news/post.html', {'menu': menu, 'post': post, 'category': category,'comments':comments,'form':form})


class Show_category(DataMixin, ListView):
    model = Post
    template_name = 'news/intro.html'
    allow_empty = False
    context_object_name = 'post'
    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['category_slug'])
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['coments']=Category.objects.all()
        mix_context = self.get_user_context(title=context['post'][0].cat)
        return dict(list(context.items()) + list(mix_context.items()))


class About(DataMixin, TemplateView):
    template_name = 'news/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mix_context = self.get_user_context(title='About Us')
        return dict(list(context.items()) + list(mix_context.items()))
