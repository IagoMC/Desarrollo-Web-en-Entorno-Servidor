from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from django.views.decorators.csrf import csrf_exempt
from .models import Tlibros, Tcomentarios
import json


def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola</h1>");

def devolver_libros(request):
	lista = Tlibros.objetos.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['titulo'] = fila_sql.titulo
		diccionario['fecha'] = fila_sql.año
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_cancion_por_id(request, id_solicitado):
	libro= Tlibros.objects.get(id = id_solicitado)
	comentarios = libro.tcomentarios_set.all()
	lista_comentarios = []
	for fila_comentario_sql in comentarios:
		diccionario = {}
		diccionario['id'] = fila_comentario_sql.id
		diccionario['comentario'] = fila_comentario_sql.comentario
		diccionario['usuario_id'] = fila_comentario_sql.usuario_id
		diccionario['libro_id'] = fila_comentario_sql.libro_id
		diccionario['fecha'] = fila_comentario_sql.fecha



		lista_comentarios.append(diccionario)
	resultado = {
		'id': libro.id,
		'titulo': libro.nombre,
		'url_imagenes': libro.url_imagen,
		'genero': libro.genero,
		'autor': libro.autor,
		'comentarios': lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def guardar_comentario(request, cancion_id):
	if request.method != 'POST':
		return None

	json_peticion = json.loads(request.body)
	comentario = Tlibros()
	comentario.comentario = json_peticion['nuevo_comentario']
	comentario.libro = Tlibros.objects.get(id = libro_id)
	comentario.save()
	return JsonResponse({"status": "ok"}) 
