from django.shortcuts import render
from .models import Article


def articles_list_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    template_name = 'article_list.html'
    return render(request, template_name, context)


def article_details(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article
    }
    template_name = 'article_details.html'
    return render(request, template_name, context)
