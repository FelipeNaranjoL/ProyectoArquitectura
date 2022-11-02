from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import formularioProducto

# Create your views here.

def home(request):
    return render(request, 'home.html')

def agregarProducto(request):
    form = formularioProducto()
    return render(request, 'agregarProducto.html',{
        'form': form
    })


def registrarse(request):
    if request.method == 'GET': 
        return render(request, 'registrarse.html',{
            'form': UserCreationForm
            })
    else:
        if request.POST ['password1'] == request.POST ['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'registrarse.html',{
                    'form': UserCreationForm,
                    "error":  "El correo ya existe"
                    })
        return render(request, 'registrarse.html',{
            'form': UserCreationForm,
            "error":  "Las contraseñas no coinciden"
            })

def cerrarSession(request):
    logout(request)
    return redirect('/')

def iniciarSession(request):
    if request.method == "GET":
        return render(request, 'iniciarSession.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciarSession.html',{
            'form': AuthenticationForm,
            'error': 'Las credenciales son incorrectas, intentanuevamente'
            })
        else:
            login(request,user)
            return redirect('home')