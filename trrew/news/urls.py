from django.contrib import admin
from django.urls import path, include

import news
from news.views import index, get_category, view_news

urlpatterns = [
    path('', index, name='main'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news')
]