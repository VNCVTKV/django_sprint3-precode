from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.values(
        'id', 'pub_date', 'location', 'text', 
        'location__is_published', 'location__name',
        'author__username',
        'category__title', 'category__slug'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).order_by('-pub_date')[:5] 
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category_ = get_object_or_404(
        Category.objects.values(
            'title', 'description'
        ).filter(is_published=True),
        slug=category_slug
    )
    posts = Post.objects.values(
        'id', 'pub_date', 'location', 'text', 
        'location__is_published', 'location__name',
        'author__username',
        'category__title', 'category__slug'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now(),
        category__slug=category_slug
    ).order_by('-pub_date')
    context = {'category': category_,
               'post_list': posts}
    return render(request, template, context)
