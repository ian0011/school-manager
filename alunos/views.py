from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Aluno
from .forms import AlunoForm


@login_required
def alunos_list(request):
    aluno = Aluno.objects.all()
    return render(request, 'alunos.html', {'aluno': aluno})


@login_required
def alunos_new(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('alunos_list')
    return render(request, 'alunos_new.html', {'form': form})
