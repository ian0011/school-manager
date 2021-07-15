from django import forms
from alunos.models import Aluno


class AlunoForm(forms.Form):
    model = Aluno
    fields = ['nome', 'cpf', 'email', 'password', 'password2']
