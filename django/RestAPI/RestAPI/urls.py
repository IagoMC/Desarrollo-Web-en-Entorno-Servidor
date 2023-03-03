from django.contrib import admin
from django.urls import path
from pai import views
#from RestAPI.views import csrf_failure
#from .views import buscar_photograpers
#from RestAPI.views import password
#from RestAPI.views import users

urlpatterns = [
 #   path('editar', views.editar_perfitl),
   # path('password', views.cambiar_contrasena),
    path('getphographers', views.buscar_photograpers),
#    path('user',views.create_user),
#    path('getagencies', views.buscar_agencies),
   # path('photographer', views.photograpers),
  #  path('agencia', views.agencia),
   # path('añadircomentariosfotografo', views.add_comment_and_rating),
   # path('añadircomentariosagencia', views.add_comment_and_rating),    
]
