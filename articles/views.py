from django.shortcuts import render, HttpResponse
from . import models


def articles_lists(request):
    articles = models.Articles.objects.all().order_by('publish_date')
    args = {'articles': articles}
    return render(request, 'articles/articles_list.html', args)


def articles_detail(request, slug):
    return HttpResponse(slug)



