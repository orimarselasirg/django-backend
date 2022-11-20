from django.urls import path
from .api import user_api_view, user_detail_api_view

urlpatterns = [
    path('usuarios/', user_api_view, name = 'usuarios '),
    path('usuarios/<int:id>/', user_detail_api_view, name = 'detalle usuario '),
]