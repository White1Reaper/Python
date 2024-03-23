from django.shortcuts import render
from django.http import HttpResponse
#Задание 1. Создать сайт на Django в соответствии с предметной областью: страховая компания.
def index(request):
    return HttpResponse("<h1>Welcome to Django!!!")