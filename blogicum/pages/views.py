"""Логика для доп. информации."""
from django.shortcuts import render


def about(request):
    """Страница с информацией о проекте."""
    template = 'pages/about.html'
    return render(request, template, {})


def rules(request):
    """Страница с правилами проекта"""
    template = 'pages/rules.html'
    return render(request, template, {})
