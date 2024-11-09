"""Логика для постов и главной страницы."""
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Category, Post


def index(request):
    """Главная страница."""
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True)[:5]
    context = {
        'post_list': post_list,
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    """Страница с полным текстом поста."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related(
            'location',
            'category',
            'author'
        ).filter(
            is_published=True,
            pub_date__lte=timezone.now()
        ),
        pk=post_id,
        category__is_published=True
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Страница с категорией поста."""
    template_name = 'blog/category.html'
    post_list = Post.objects.select_related(
        'location',
        'category',
        'author'
    ).filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__slug=category_slug,
    )
    category = get_object_or_404(
        Category.objects.values(
            'title',
            'description'
        ),
        slug=category_slug,
        is_published=True
    )
    context = {'post_list': post_list,
               'category': category}
    return render(request, template_name, context)
