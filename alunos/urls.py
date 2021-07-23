from django.urls import path
from .views import alunos_list
from .views import alunos_new
from .views import alunos_update
from .views import alunos_delete
urlpatterns = [
    path('list/', alunos_list, name="alunos_list"),
    path('new/', alunos_new, name="alunos_new"),
    path('update/<int:id>', alunos_update, name="alunos_update"),
    path('delete/<int:id>', alunos_delete, name="alunos_delete"),
]
