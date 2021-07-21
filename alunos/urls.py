from django.urls import path
from .views import alunos_list

urlpatterns = [
    path('list/', alunos_list, name="alunos_list"),
]
