from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list_view, name='article'),
    path('article/<int:id>/', views.article_details, name='article_details'),
]
