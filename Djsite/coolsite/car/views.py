from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models  import *

menu = ["О сайте", "Партнёрам", "Обратная связь", "Войти"]

# Create your views here.
def index(request):
    posts = Car.objects.all()
    return render(request, 'car/index.html', {'posts':posts , 'menu':menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'car/about.html', {'menu':menu, 'title':'О сайте'}) 

def categories(request, carid):
    print (request.GET)
    return HttpResponse(f"<h1>Категории<h1><p>{carid}<p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    
    return HttpResponse(f"<h1>Архив по годам<h1><p>{year}<p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')