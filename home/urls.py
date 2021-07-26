from django.urls import path
from .views import home, my_logout, alunos_list, alunos_new

urlpatterns = [
    path('', home, name="home"),
    path('logout/', my_logout, name="logout"),
    path('list/', alunos_list, name="alunos_list"),
    path('new/', alunos_new, name="alunos_new")
]
