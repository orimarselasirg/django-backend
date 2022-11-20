from django.urls import path
from .api import task_api_view, task_api_view_creator, task_api_view_search

urlpatterns = [
    path('tareas/<int:id>/', task_api_view, name = 'tareas'),
    path('tareas/', task_api_view_creator, name = 'crear tareas'),
    path('modificar/<int:id>/', task_api_view, name = 'modificar tareas'),
    path('eliminar/<int:id>/', task_api_view, name = 'eliminar tareas'),
    path('completar/<int:id>/', task_api_view, name = 'completar tareas'),
    path('buscar/<str:task>', task_api_view_search, name = 'buscar tareas'),
]