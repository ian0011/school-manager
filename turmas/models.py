from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={
        'groups_name': "Docente"}, verbose_name="Professor")
    email = models.EmailField(
        max_length=255, default='', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Turma(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    local = models.charField(max_length=255)
    data = models.datetimeField(auto_now=False, auto_now_add=False)
    qtde_vagas = models.DecimalField(
        max_digits=5, decimal_places=0, verbose_name="Vagas")
    qtde_visitantes = models.DecimalField(
        max_digits=5, decimal_places=0, verbose_name="Visitantes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    user_locado = models.IntegerField(blank=True, null=True)
