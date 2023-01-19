from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Fotografo, Agencia
from array import array

import json

def home (request):
	Maximo_fotografos = Fotografo
	Maximo_agencias = Agencia.objetos.all()
	
	AleatorioFotografo = randrage(1, Maximo_fotografos,1)
	AleatorioAgencia = randrage(1, Maximo_agencias,1)
	

	# Carrusel
	aleatorio = randrage(1,2,1)
	
	if aleatorio==1 :
		#Metemos imagen y descripciom
	else:
		#Metemos imagen y descripcion

	#
	Filas = array("i",[0,0,0,0,0,0])

	

	for indice1 in 6:
		
	if aleatorio ==1:
		aleatorioF=randger(1,mf,1)
			for(1 in 6):
				if (aleatorioF =

			Maximo_fotografos = Fotografo
			Maximo_agencias = Agencia.objetos.all()
			
			AleatorioFotografo = randrage(1, Maximo_fotografos,1)
			AleatorioAgencia = randrage(1, Maximo_agencias,1)
						


			aleatorio2= randrage(1,2,1)
				
			 
				if aleatorio2==1:
				
				else:

		
# Create your views here.
