from django.shortcuts import render, get_object_or_404
from .models import Article


def desert_geeks(request):
    articles = Article.objects
    return render(request, 'articles/home.html', {'articles': articles})


def detail(request, article_id):
    article_detail = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/detail.html', {'article': article_detail})