from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import AddNewForm
from .models import News, Category


class NewsList(ListView):
    model = News
    template_name = 'news/main.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Новости POE"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ByCategoryList(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{Category.objects.get(pk=self.kwargs['category_id'])}"
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNew(DetailView):
    model = News
    template_name = 'news/show_new.html'
    context_object_name = 'new'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{News.objects.get(pk=self.kwargs['pk'])}"
        return context


class AddNews(CreateView):
    form_class = AddNewForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('main')

