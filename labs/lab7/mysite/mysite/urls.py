
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mmm/',index),
    path('', main_page, name='main_page'),
]
