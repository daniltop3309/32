from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


def styl(request):
    return render(request, 'index.html')

def post(request):
    name = request.POST.get('name', 'Undefined')
    email = request.POST.get('email', 'Undefined')
    phone = request.POST.get('phone', 'Undefined')
    service = request.POST.get('service', 'Undefined')
    return HttpResponse(f'''
    <p>name: {name}</p>
    <p>email: {email}</p>
    <p>phone: {phone}</p>
    <p>service: {service}</p>''')

# 2 задание

# def styl(request):
#     userform = UserForm()
#     return render(request, 'index.html', {'form': userform})

# def index(request):
#     userform = UserForm()
#     return render(request, 'index.html', {'form': userform})

# def post1(request):
#     name = request.POST.get('name', 'Undefined')
#     surname = request.POST.get('surname', 'Undefined')
#     country = request.POST.get('country', 'Undefined')
#     region = request.POST.get('region', 'Undefined')
#     street = request.POST.get('street', 'Undefined')
#     return HttpResponse(f'''
#     <p>Убедитесь, что адрес правильный,{name} {surname}</p>
#     <p>{country}</p>
#     <p>{region}</p>
#     <p>{street}</p>''')
