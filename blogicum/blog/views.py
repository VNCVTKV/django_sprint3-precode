from django.shortcuts import render



def index(request):
    template = 'blog/index.html'
    reversed_posts = posts[::-1]
    context = {'posts': reversed_posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    context = {'post': posts[id]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
