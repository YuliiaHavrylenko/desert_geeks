from django.shortcuts import render
from .models import Article


def desert_geeks(request):
    articles = Article.objects
    return render(request, 'articles/home.html', {'articles': articles})
