# Create your views here.
import json
from datetime import datetime

from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        # Get all previous data from parent class
        context = super().get_context_data(**kwargs)
        # Create your own data
        context['news_title'] = 'Громкий новостной заголовок'
        context['news_preview'] = 'Предварительное описание, которое заинтересует каждого'
        context['range'] = range(5)
        context['datetime_obj'] = datetime.now()
        # добавил чтение новостей из файла json
        # added load news from json-file
        with open('mainapp/templates/mainapp/news.json', 'r', encoding='utf-8') as file:
            news = json.load(file)
            context['news'] = news
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context['page_num'] = page
        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'
