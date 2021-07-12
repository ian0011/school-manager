from django.shortcuts import render


def view_alunos(request):
    return render(request, 'alunos.html', {})
