from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno
from django.http import HttpResponseRedirect
from django.urls import reverse
from alunos.forms import AlunoForm


@login_required
def alunos_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})


@login_required
def alunos_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('alunos')
