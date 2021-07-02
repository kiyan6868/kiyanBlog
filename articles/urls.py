from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('', views.articles_lists, name="list"),
    path('<slug>', views.articles_detail, name="detail"),
]