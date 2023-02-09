from django.contrib import admin
from django.urls import path
from pai import views

urlpatterns = [
    path('editar', views.editar_perfitl),
    path('password', views.cambiar_contraseña),
    path('getphographers', views.buscar_photograpers),
    path('getagencies', views.buscar_agencies),
    path('photographer', views.photographer),
    path('agencia', views.agencia),
    path('añadircomentariosfotografo', views.add_comment_and_rating),
    path('añadircomentariosagencia', views.add_comment_and_rating),    
]
