from django.contrib import admin
from django.urls import path, include

import news
from news.views import NewsList, ViewNew, ByCategoryList, AddNews

urlpatterns = [
    path('', NewsList.as_view(), name='main'),
    path('category/<int:category_id>/', ByCategoryList.as_view(), name='category'),
    path('news/<int:pk>/', ViewNew.as_view(), name='view_news'),
    path('news/add_news/', AddNews.as_view(), name='add_news')
]