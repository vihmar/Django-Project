from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        
        if user:
            login_django(request,user)
            return plataforma(request)
        else:
            return HttpResponse('usuario e senha invalido')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        username = request.POST.get('username')
        data = request.POST.get('data')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com este username')

        user = User.objects.create_user(username=username, password=senha, date_joined=data)
        user.save()

        return login(request)

def plataforma(request):
    if request.user.is_authenticated:
        lista = User.objects.all()
        context = {
            'lista' : lista
        }
        return render(request, 'plataforma.html', context)
    else:
        return HttpResponse('Você precisa estar logado')



