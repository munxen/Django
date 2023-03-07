from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models  import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Партнёрам", 'url_name': 'partners'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]
# Create your views here.
def index(request):
    posts = Car.objects.all()
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'}
    return render(request, 'car/index.html',context = context)

def about(request):
    return render(request, 'car/about.html', {'menu':menu, 'title':'О сайте'}) 

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def partners(request):
    return HttpResponse ("Партнёрам")

def contact(request):
    return HttpResponse ("Обратная связь")

def login(request):
    return HttpResponse ("Авторизация")

def show_post(request, post_id):
    return HttpResponse (f"Отображение статьи с id = {post_id}")