from django import forms
from .models import Aluno


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome',)
