
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mmm/',index),
    path('', main_page, name='main_page'),
    # Задание 7. Возможность модифицирования данных в моделях со стороны клиентской части.
    path('update_client/<int:client_id>/', update_client, name='update_client'),
    path('delete_client/<int:client_id>/', delete_client, name='delete_client'),
]
