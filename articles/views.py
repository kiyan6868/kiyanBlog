from django.shortcuts import render, HttpResponse
from . import models


def articles_lists(request):
    articles = models.Articles.objects.all().order_by('-publish_date')
    args = {'articles': articles}
    return render(request, 'articles/articles_list.html', args)


def articles_detail(request, slug):
    article_detail = models.Articles.objects.get(slug=slug)
    args = {'article_detail' : article_detail}
    return render(request, 'articles/article_details.html', args)



