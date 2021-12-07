import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    current_dir = os.getcwd()
    workdir_list = os.listdir(path= current_dir)
    total = []
    for i in workdir_list:
        if len(total) == len(workdir_list) - 1:
            total.append(f'\n - {i}.')
        else:
            total.append(f'\n - {i},')
    return HttpResponse(total)
