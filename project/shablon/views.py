from django.shortcuts import render
from .models import ListNews
from datetime import datetime
from django.views.generic import ListView, DetailView
# Create your views here.

class Article(ListView):
    model = ListNews
    ordering = '-data_cr_st'
    template_name = 'main.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class ArticleId(DetailView):
    model = ListNews
    template_name = 'news.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context
