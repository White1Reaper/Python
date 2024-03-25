from django.shortcuts import *
from django.http import HttpResponse
#Задание 1. Создать сайт на Django в соответствии с предметной областью: страховая компания.
def index(request):
    return HttpResponse("<h1>Welcome to Django!!!")


from .models import *


def main_page(request):
    clients = Client.objects.all()
    return render(request, 'main_page.html', {'clients': clients})


#Задание 7. Возможность модифицирования данных в моделях со стороны клиентской части.
def update_client(request, client_id):
    client = Client.objects.get(id=client_id)

    if request.method == 'POST':
        client.first_name = request.POST.get('first_name')
        client.last_name = request.POST.get('last_name')
        client.email = request.POST.get('email')
        client.save()
        return redirect('main_page')

    return render(request, 'update_client.html', {'client': client})


def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('main_page')