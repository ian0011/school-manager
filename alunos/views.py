from alunos.models import Aluno
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from alunos.forms import AlunoForm


def view_alunos(request):
    aluno_instance = get_object_or_404(Aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            aluno_instance.save()

            return HttpResponseRedirect(reverse('all-borrowed'))
    else:
        form = ''
        context = {
            'form': form,
            'aluno_instance': aluno_instance
        }
    return render(request, 'alunos.html', context)
