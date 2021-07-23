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


@login_required
def alunos_update(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('alunos_list')

    return render(request, 'alunos_new.html', {'form': form})


@login_required
def alunos_delete(request, id):
    aluno = get_object_or_404(Aluno, pk=id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos_list')

    return render(request, 'aluno_delete_confirm.html', {'aluno': aluno})
