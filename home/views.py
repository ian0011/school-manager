from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


def alunos_list(request):
    return render(request, 'alunos.html')


def alunos_new(request):
    return render(request, 'alunos_new.html')
