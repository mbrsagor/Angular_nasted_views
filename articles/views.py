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
    if id is not None:
        article = Article.objects.get(id=id)
        context = {
            'article': article
        }
        template_name = 'article_details.html'
        return render(request, template_name, context)
    else:
        return False


def article_search_view(request):
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET  # This is a dictionary
    article_obj = None
    try:
        query = int(query_dict.get("q")) # <input type="text" name="q" />
    except:
        query = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    template_name = 'search.html'
    return render(request, template_name, {"object": article_obj})
