from django.db import models
from django.utils import timezone


class Aluno(models.Model):
    nome = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=14, null=False, verbose_name="CPF")
    email = models.EmailField(max_length=254, null=False)
    telefone = models.CharField(max_length=16, null=True)
    created_date = models.DateField(default=timezone.now)
