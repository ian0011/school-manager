from django.urls import path
from .views import alunos_list
from .views import alunos_new
urlpatterns = [
    path('list/', alunos_list, name="alunos_list"),
    path('new/', alunos_new, name="alunos_new"),
]
