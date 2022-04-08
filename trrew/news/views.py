from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
                }
    return render(request, 'news/main.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': f'Категория: { category }',
                }
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    new = get_object_or_404(News, pk=news_id)
    context = {
        'new': new,
        'title': new.title,
                }
    return render(request, 'news/show_new.html', context)