

from random import randrange
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import models
from .models import (Clientes, Fotografo, Agencia, Comentariofotografo)
#from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Q
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.contrib.auth import authenticate, login
#from django.contrib.auth.views import login

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from random import choices
from string import ascii_uppercase, digits
import json
import random
import string

from django.core.paginator import Paginator

@require_GET
def buscar_photographers(request):
    # Obtener el parámetro "query" de la petición GET
    query = request.GET.get("query")
    # Obtener todos los objetos Fotografo de la base de datos
    photographers = Fotografo.objects.all()

    # Filtrar por consulta
    if query:
        # Convertir la consulta a minúsculas
        query = query.lower()
        # Filtrar los objetos Fotografo por nombre, descripción y ciudad que contengan la consulta
        photographers = photographers.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query)
        )

    # Calcular la media de valoración para cada fotógrafo en la lista de resultados
    for photographer in photographers:
        photographer.media_valoracion = photographer.comentariofotografo_set.aggregate(Avg('valoracion'))['valoracion__avg']

    # Obtener el parámetro "size" de la petición GET
    size = request.GET.get("size")
    if size:
        try:
            # Convertir el tamaño de página a un entero
            size = int(size)
            # Si el tamaño de página es menor que 1, no se usa paginación
            if size < 1:
                size = None
        except ValueError:
            # Si el tamaño de página no es un entero válido, no se usa paginación
            size = None

    # Filtrar por media de valoración si se ha especificado una media válida
    media = request.GET.get("media")
    if media:
        try:
            # Convertir la media a un número decimal
            media = float(media)
        except ValueError:
            # Si la media no es un número decimal válido, no se filtra por media
            media = None

        # Filtrar por media de valoración si se ha especificado una media válida
        if media:
            photographers = photographers.filter(media_valoracion__gte=media)

    # Paginar los resultados de la consulta si se ha especificado un tamaño de página válido
    if size:
        # Crear un objeto Paginator con la lista de objetos Fotografo y el tamaño de página
        paginator = Paginator(photographers, size)
        # Obtener el número de página actual de la petición GET
        page_number = request.GET.get("page")
        # Obtener el objeto Page correspondiente a la página actual
        page_obj = paginator.get_page(page_number)
        # Actualizar la lista de objetos Fotografo con los objetos de la página actual
        photographers = page_obj.object_list

    # Crear una lista vacía para almacenar los resultados de la consulta
    data = []
    for photographer in photographers:
        # Para cada objeto Fotografo, agregar un diccionario con sus datos a la lista "data"
        data.append(
            {
                "id": photographer.id,
                "name": photographer.nombre,
                "apellido": photographer.apellido,
                "description": photographer.descripcion,
                "email": photographer.email,
                "telefono": photographer.telefono,
                "ciudad": photographer.ciudad,
                "tiktok": photographer.tiktok,
                "twitter": photographer.twitter,
                "instagram": photographer.instagram,
                "fotoperfil": photographer.fotoperfil,
                "media": photographer.media_valoracion
            }
        )

    # Si no se ha especificado ninguna consulta ni tamaño de página, devolver todos los objetos Fotografo
    if not query and not size:
        return JsonResponse(data, safe=False)
    # Si se ha especificado un tamaño de página, devolver la página actual y la información de paginación
    elif size:
        return JsonResponse({
            #"count": paginator.count,
            #"num_pages": paginator
            #"page_range": list(paginator.page_range),
            "results": data
        }, safe=False)
    # Si se ha especificado una consulta pero no un tamaño de página, devolver los resultados sin paginación
    else:
        return JsonResponse(data, safe=False)

		
@csrf_exempt
def ruser(request):
    if request.method == 'POST':
        # parsear el cuerpo de la solicitud
        bodyunicode = request.body.decode('utf-8')
        body = json.loads(bodyunicode)
        
        # validar campos requeridos
        campos_requeridos = ['type', 'id', 'email', 'nombre', 'contrasena', 'ccontrasena', 'telefono', 'ciudad']
        for campo in campos_requeridos:
            if campo not in body:
                return JsonResponse({'error': f'Falta campo requerido: {campo}'}, status=400)
        
        # validar que los campos de contraseña coincidan
        if body['contrasena'] != body['ccontrasena']:
            return JsonResponse({'error': 'Los campos de contraseña no coinciden'}, status=400)
        
        # crear usuario
        tipo_usuario = body['type']
        id = int(body['id'])  # convertir el valor de "id" de string a int
        email = body['email']
        nombre = body['nombre']
        contrasena = body['contrasena']
        telefono = int(body['telefono'])  # convertir el valor de "telefono" de string a int
        ciudad = body['ciudad']
        modelos_usuario = {
            'Agencia': Agencia,
            'Clientes': Clientes,
            'Fotografo': Fotografo,
        }
        if tipo_usuario in modelos_usuario:
            try:
                usuario_modelo = modelos_usuario[tipo_usuario]
                if usuario_modelo.objects.filter(email=email).exists():
                    return JsonResponse({'error': 'La dirección de correo electrónico ya está en uso'}, status=400, safe=False)
                usuario = usuario_modelo(id=id, email=email, nombre=nombre,contrasena=contrasena, telefono=telefono, ciudad=ciudad)
                #usuario.set_password(contrasena)
                usuario.save()
                return JsonResponse({'success': f'Se creó el usuario {email}'}, status=201, safe=False)
            except Exception as e:
                return JsonResponse({'error': f'No se pudo crear el usuario: {e}'}, status=500, safe=False)
        else:
            return JsonResponse({'error': f'Tipo de usuario no válido: {tipo_usuario}'}, status=400, safe=False)


@csrf_exempt
def loguearse(request):
 if request.method == 'POST':

    data = json.loads(request.body)
    email = data.get('email')
    contrasena = data.get('contrasena')

    if not email or not contrasena:
        return JsonResponse({'error': 'Faltan datos en el cuerpo'}, status=400, safe=False)

    try:
        usuario = Clientes.objects.get(email=email)
    except Clientes.DoesNotExist:
        try:
            usuario = Fotografo.objects.get(email=email)
        except Fotografo.DoesNotExist:
            try:
                usuario = Agencia.objects.get(email=email)
            except Agencia.DoesNotExist:
                return JsonResponse({'error': 'No se encontró el usuario'}, status=404, safe=False)

    if usuario.contrasena != contrasena:
        return JsonResponse({'error': 'Contraseña incorrecta'}, status=401, safe=False)

    token = ''.join(choices(ascii_uppercase + digits, k=6))
    #Sesion.objects.create(usuario=usuario, token=token)

    return JsonResponse({'sesiontoken': token}, status=201, safe=False)

@csrf_exempt
def aComentaris(request, fotografo_id):
    if request.method == 'POST':
        token = request.headers.get('token')
        data = json.loads(request.body)
        comentario = data.get('comentario')
        rating = data.get('rating')

        if not comentario or not rating:
            return JsonResponse({'error': 'Faltan datos en el cuerpo'}, status=400)

        try:
            fotografo = Fotografo.objects.get(id=fotografo_id)
        except Fotografo.DoesNotExist:
            return JsonResponse({'error': 'Fotógrafo no encontrado'}, status=404)

        try:
            usuario = Clientes.objects.get(token=token)
        except Clientes.DoesNotExist:
            return JsonResponse({'error': 'No autorizado'}, status=404)

        comentarioFotografo = Comentariofotografo.objects.create(
            id=Comentariofotografo.objects.count()+1,
            idusuario=usuario,
            idfotografo=fotografo,
            comentario=comentario,
            valoracion=int(rating),
        )
        return JsonResponse({'message': 'Comentario y valoración publicados'}, status=201)  
"""
ValueError: Cannot assign "9": "Comentariofotografo.idusuario" must be a "Clientes" instance.
ValueError: Cannot assign "<Agencia: Agencia object (1)>": "Comentariofotografo.idusuario" must be a "Clientes" instance.
ValueError: Cannot assign "1": "Comentariofotografo.idusuario" must be a "Clientes" instance.
RuntimeError: You called this URL via POST, but the URL doesn't end in a slash and you have APPEND_SLASH set. Django can't redirect to the slash URL while maintaining POST data. Change your form to point to localhost:8000/fotografos/26/comentarios/ (note the trailing slash), or set APPEND_SLASH=False in your Django settings.
from array import array
from django.db import models
#from django.contrib.auth.hashers import hashpw, gensalt
from django.db.models import Q
#from django.views.decorators.csrf import csrf_exempt
import jwt
import json
import pai.views
import string
import random
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from django.conf import settings
from django.contrib.auth import authenticate

#Crear Usuario
import random
import string
from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt

def create_user(request):
    # Obtener los datos del body del request
    data = json.loads(request.body)
    user_type = data.get('type')
    email = data.get('email')
    nombre = data.get('nombre')
    contrasena = data.get('contrasena')
    CContrasena = data.get('CContrasena')

    # Validar que los datos del request sean válidos
    if not user_type or not email or not nombre or not contrasena or not CContrasena:
        return JsonResponse({'error': 'Faltan datos en el request'}, status=400)
    if contrasena != CContrasena:
        return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)

    try:
        token = ''.join(random.choices(string.ascii_letters, k=6))

        # Insertar el nuevo usuario en la base de datos
        if user_type == 'Clientes':
            Cliente = Clientes.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Cliente creado correctamente', 'token': token}, status=201)
        elif user_type == 'Fotografo':
            Fotografo = Fotografo.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Fotografo creado correctamente', 'token': token}, status=201)
        elif user_type == 'Agencia':
            Agencia = Agencia.objects.create(
                email=email,
                contrasena=contrasena,
                name=nombre,
                token=token
            )
            return JsonResponse({'success': 'Agencia creada correctamente', 'token': token}, status=201)
        else:
            return JsonResponse({'error': 'Tipo de usuario no válido'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
	
"""
"""
def home (request):
	Maximo_fotografos = Fotografo
	Maximo_agencias = Agencia.objetos.all()
	
	AleatorioFotografo = randrange(1, Maximo_fotografos,1)
	AleatorioAgencia = randrange(1, Maximo_agencias,1)
	
	# Carrusel
	aleatorio = randrange(1,2,1)
	
	if aleatorio==1:
        a=2
		#Metemos imagen y descripcion
	else:
        a=1
    		#Metemos imagen y descripcion
	#
	
Filas = [[0, 0, 0,0,0,0], [0,0]]
numero=0
fuera=0
foto=0
i=0
indice=0
Agencia=0
aleatorio = randrange(1,2,1)
if aleatorio ==1:
	while foto<6:
		AleatorioFotografo=randrange(1,Maximo_fotografos,1)
		while numero<6 and fuera==0:
			for i in 6:
					if Filas(i,1)==AleatorioFotografo:
						fuera=1
					else:
						numero=numero+1
		if numero==6:
			Filas(indice,1)==AleatorioFotografo
			Filas(indice,2)==1#Descripcion 
			foto=foto+1
		indice=indice+1
else:
	while Agencia<6:
		AleatorioAgencia=randrange(1,Maximo_agencias,1)
		while numero<6 and fuera==0:
			for i in 6:
					if Filas(i,1)==AleatorioAgencia:
						fuera=1
					else:
						numero=numero+1
		if numero==6:
			Filas(indice,1)==AleatorioAgencia
			Filas(indice,2)==1#Descripcion 
			foto=foto+1
		indice=indice+1
		
"""

"""
@csrf_exempt
def cambiar_contrasena(request):
	if request.method == "POST":
		#pillamos los datos del body
		json_load =json.loads(request.body)
		#pillamos la contraseña antigua
		contrasenaAntigua=json_load['contrasenaAntigua'] #dentro de los [] metemos el valor en react
		#pillamos la contraseña nueva
		ContrasenaNueva=json_load['ContrasenaNueva']
		#pillamos la repeticion de la contraseña nueva 
		ContrasenaNueva2=json_load['ContrasenaNueva2']

			# Validamos la contraseña
		if ContrasenaNueva!=ContrasenaNueva2:
			return JsonResponse({'error': 'No coinciden'}, status=400)
		else:
			#Cogemos el token en la cabecera
			tokens = request.headers.get('token')
			clientes=Clientes.objects.get(token=tokens)
			if clientes==None:
				return JsonResponse({'error': 'Invalid token'}, status=401)

			else:
				#cliente = Clientes.objects.get(token=tokens ) #seleccionamos el cliente con el token
				if check_password(contrasenaAntigua, cliente.contrasena): #Validamos que la contraseña Antigua es del cliente

						cliente.contrasena=set_password(ContrasenaNueva) #Cambiamos la contraseña
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						cliente.save()
				else:
					return JsonResponse({'error': 'contraseña incorrecta'}, status=403)

"""
"""
			#Hacemos lo mismo en fotografos y agencias
			elif Fotografo.objects.get(token=tokens )== None:
				fotografo = Fotografo.objects.get(token=tokens )
				if check_password(contraseñaAntigua, fotografo.contraseña):
						fotografo.contraseña=set_password(ContraseñaNueva)
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						fotografo.save()
				else:
					return JsonResponse({'error': 'old_password incorrecta'}, status=403)
			elif Agencia.objects.get(token=tokens )==None:
				agencia = Agencia.objects.get(token=tokens )
				if check_password(contraseñaAntigua, agencia.contraseña):
						agencia.contraseña=set_password(ContraseñaNueva)
						#sentencias para cambiar la contraseña
						print('contraseña cambiada')
						agencia.save()
				else:
					return JsonResponse({'error': 'old_password incorrecta'}, status=403)
	
	
"""
#################################################		
"""
def editar_perfitl(reques):
	#cogemos los datos del cuerpo
	cuerpo =json.loads(request.body)
	#cogemos el token de la cabecera
	tokens = json.loads(request.header)
	if not tokens or tokens != token:
		return JsonResponse({'error': 'Invalid token'}, status=401)
	#Cogemos el cliente con el token
	cliente = Clientes.objects.get(token=tokens )
	#Cogemos el fotografo con el token
	fotografo = Fotografo.objects.get(token=tokens )
	#Cogemos el agencia con el token
	agencia= Agencia.objects.get(token=tokens )
	
#Preguntamos si el cliente esta vacio 
	if cliente!=None:
		#Pillamos lod datos del cuerpo
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_usuario=json['usuario']
		editar_correo=json['correo']
		editar_fotoperfil=json['fotoPerfil']
		#Modificamos los datos si no estan vacios, es decir si no se van a modificar
		if editar_NombreUsuario!="":
			cliente.nombre = editar_NombreUsuario #modificamos los datos
		if editar_Descripcion!="":
			cliente.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			cliente.telefono = editar_numeroTelefono
		if editar_usuario!="":
			cliente.usuario = editar_usuario
		if editar_correo!="":
			cliente.email = editar_correo
		if editar_fotoperfil!="":
			cliente.fotoperfil= editar_fotoperfil
		cliente.save()
#Igual que para agencia y fotografo
	elif fotografo!=None:
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_usuario=json['usuario']
		editar_correo=json['correo']
		editar_ciudad=json['ciudad']
		editar_fotoperfil=json['fotoPerfil']
		editar_tiktok=json['tiktok']
		editar_instagram= json['instagram']
		editar_twitter= json['facebook']
		if editar_NombreUsuario!="":
			fotografo.nombre = editar_NombreUsuario
		if editar_Descripcion!="":
			fotografo.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			fotografo.telefono = editar_numeroTelefono
		if editar_usuario!="":
			fotografo.usuario = editar_usuario
		if editar_correo!="":
			fotografo.email = editar_correo
		if editar_fotoperfil!="":
			fotografo.fotoperfil= editar_fotoperfil
		if editar_tiktok!="":
			fotografo.tiktok=editar_tiktok
		if editar_twitter!="":
			fotografo.twitter=editar_twitter
		if editar_instagram!="":
			fotografo.instagram=editar_twitter
		if editar_ciudad!="":
			fotografo.ciudad=editar_ciudad		
		fotografo.save()
	elif agencia!=None:
		editar_NombreUsuario=json['nombreUsuario']
		editar_Descripcion=json['Descripcion']
		editar_numeroTelefono=json['NumeroTelefono']
		editar_correo=json['correo']
		editar_ciudad=json['ciudad']
		editar_fotoperfil=json['fotoPerfil']
		editar_tiktok=json['tiktok']
		editar_instagram= json['instagram']
		editar_twitter= json['facebook']		
		if editar_NombreUsuario!="":
			agencia.nombre = editar_NombreUsuario
		if editar_Descripcion!="":
			agencia.descripcion = editar_Descripcion
		if editar_numeroTelefono!="":
			agencia.telefono = editar_numeroTelefono
		if editar_correo!="":
			agencia.email = editar_correo
		if editar_fotoperfil!="":
			agencia.fotoperfil= editar_fotoperfil
		if editar_tiktok!="":
			agencia.tiktok=editar_tiktok
		if editar_twitter!="":
			agencia.twitter=editar_twitter
		if editar_instagram!="":
			agencia.instagram=editar_twitter
		if editar_ciudad!="":
			agencia.ciudad=editar_ciudad	
		agencia.save()
	realizamos varias sentencias para seleccionar la busqueda correcta
	# si query no esta vacio y rating esta vacio realziamos esta busqueda
	if query!="" and rating=="":
			i=1
			#cogemos todos los datos de fotografo quye cumplen con las siguientes sentencias
			fotografo = Fotografo.objects.get(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			resultado = []
			#coge ln numero de fotografos que indica el size
			while i< len(fotografo) and i<size:
				resultado= ({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
						}	)
				i=i+1
				media=0
		
# si query no esta vacio y rating no esta vacio realziamos esta busqueda	
	if query!="" and rating!="":
			#cogemos todos los datos de fotografo quye cumplen con las siguientes sentencias
			fotografo = Fotografo.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			i=1
			imedia=0
			resultado = []
			#tambien pillamos la media de cada fotografo
			while i< len(fotografo) and imedia<size:
				comentarios = Comentariofotografo.objects.filter(idfotografo=fotografo[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentariofotografo.valoracion
				media = suma_valoracion / num_comentarios
				#si el rating es el mismo que la media se muestra los siguientes datos
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
							}	)
					num_comentarios=0
					suma_valoracion=0
					media=0		
					
					i=i+1
#si query esta vacio y rating no, realiza la siguiente busqueda
	if query=="" and rating!="":
			fotografo = Fotografo.objects.all()
			i=1
			imedia=0
			resultado = []
			while i< len(fotografo) and imedia<size:
				comentarios = Comentariofotografo.objects.filter(idfotografo=fotografo[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentariofotografo.valoracion
				media = suma_valoracion / num_comentarios
				#si el rating es el mismo que la media se muestra los siguientes datos
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
							}	)
					num_comentarios=0
					suma_valoracion=0
					media=0		
					
					i=i+1
#si query esta vacio y rating tambien, realizamos la siguiente busqueda. Selecciona por orden, no tiene filtro
	if query=="" and rating=="":
			fotografo = Fotografo.objects.all()
			i=1
			resultado = []
			while i< len(fotografo) and i<size:
				
				resultado.append({
								'id': fotografo[i].id,
								'Nombre': fotografo[i].nombre,
								'FotoPerfil': fotografo[i].fotoperfil,
	
							}	)
				media=0		
					
				i=i+1			
#El funcionamiento es simialr a la funcion anterior
"""
"""
def buscar_agencies(request):
	
	query=json['query']
	size=json['size']
	rating=json['rating']
	rated_under=json['rated_under']
	if query!="" and rating=="":
			i=1
			agencia = Agencia.objects.get(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			resultado = []
			while i< len(agencia) and i<size:
				
				resultado= ({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
			
								'FotoPerfil': agencia[i].fotoperfil,
						}	)
				i=i+1
			
		
	if query!="" and rating!="":
			agencia = Agencias.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query) | Q(ciudad__icontains=query) )
			i=1
			imedia=0
			resultado = []
			while i< len(agencia) and imedia<size:
				comentarios = Comentarioagencia.objects.filter(idagencia=agencia[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentarioagencia.valoracion
				media = suma_valoracion / num_comentarios
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
							
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
				num_comentarios=0
				suma_valoracion=0
				media=0		
					
				i=i+1
	if query=="" and rating!="":
			agencia = Agencias.objects.all()
			i=1
			imedia=0
			resultado = []
			while i< len(agencia) and imedia<size:
				comentarios = Comentarioagencia.objects.filter(idagencia=agencia[i].id)
				for comment in comentarios:
					num_comentarios += 1
					suma_valoracion += Comentarioagencia.valoracion
				media = suma_valoracion / num_comentarios
				if rating==media:
					imedia=imedia+1
					resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
				num_comentarios=0
				suma_valoracion=0
				media=0		
					
				i=i+1
	if query=="" and rating=="":
			agencia = Agencias.objects.all()
			i=1
			resultado = []
			while i< len(agencia) and i<size:
				
				resultado.append({
								'id': agencia[i].id,
								'Nombre': agencia[i].nombre,
								'FotoPerfil': agencia[i].fotoperfil,
							}	)
					
				i=i+1			
"""

#Aarón Saavedra Lagares
"""
def photographer (request):
    if request.method == 'GET':
        JsonResponse=[]
        resultado=[]
        id = request.GET['id']
        fotografo = Fotografo()
        fotografo= Fotografo.objects.get(id=id)
        if fotografo==None:
            print('Este fotograf@ no se corresponde con ningun id')
        
        else:
            resultado={
                'id' : fotografo.id,
                'name' : fotografo.name,
                'description' : fotografo.description,
                'phone' : fotografo.phone,
                'instagram' : fotografo.instagram,
                'twitter' : fotografo.twitter,
                'tiktok' : fotografo.tiktok,
                'photo' : fotografo.photo,
                'averageRaiting' : fotografo.averageRaiting
            }
    return JsonResponse (resultado, json_dumps_params={'ensurce_ascii': False})
@csfr_exempt
def agencia (request):
    if request.method == 'GET':
        JsonResponse=[]
        resultado=[]
        id = request.GET['id']
        agencia = Agencia()
        agencia= Agencia.objects.get(id=id)
        if agencia==None:
            print('Este fotograf@ no se corresponde con ningun id')
        
        else:
            resultado={
                'id' : agencia.id,
                'name' : agencia.name,
                'description' : agencia.description,
                'phone' : agencia.phone,
                'instagram' : agencia.instagram,
                'twitter' : agencia.twitter,
                'tiktok' : agencia.tiktok,
                'photo' : agencia.photo,
                'averageRaiting' : agencia.averageRaiting
            }
    return JsonResponse (resultado, json_dumps_params={'ensurce_ascii': False})
@csfr_exempt
# Para utilizar Flask, primero debes instalarlo en tu entorno de desarrollo. Puedes hacerlo utilizando el gestor de paquetes de Python, pip, con el siguiente comando:
# pip install Flask
app = Flask(id)
Comentariofotografo = {
    1: {'comments': [], 'ratings': []},
    2: {'comments': [], 'ratings': []}
}
@app.route('/Comentariofotografo/<int:id>/comments', methods=['POST'])
def add_comment_and_rating(id):
    if id not in Comentariofotografo:
        return jsonify({'message': 'Fotografo no encontrado'}), 404
    if 'SessionToken' not in request.headers:
        return jsonify({'message': 'No estas autorizado'}), 401
    if 'SessionToken' != request.headers['SessionToken']:
        return jsonify({'message': 'No estas autorizado'}), 401
    comment = request.json.get('new_comment')
    rating = request.json.get('new_rating')
    if not comment or not rating:
        return jsonify({'message': 'Bad Request'}), 400
    Comentariofotografo[id]['comentario'].append(comment)
    Comentariofotografo[id]['valoracion'].append(rating)
    return jsonify({'message': 'Comentario y valoración añadidas correctamente'}), 201
if id == '__main__':
    app.run()
@csfr_exempt
app = Flask(id)
Comentarioagencia = {
    1: {'comments': [], 'ratings': []},
    2: {'comments': [], 'ratings': []}
}
@app.route('/Agencia/<int:id>/comments', methods=['POST'])
def add_comment_and_rating(id):
    if id not in Comentarioagencia:
        return jsonify({'message': 'Agencia no encontrado'}), 404
    if 'SessionToken' not in request.headers:
        return jsonify({'message': 'No estas autorizado'}), 401
    if 'SessionToken' != request.headers['SessionToken']:
        return jsonify({'message': 'No estas autorizado'}), 401
    comment = request.json.get('new_comment')
    rating = request.json.get('new_rating')
    if not comment or not rating:
        return jsonify({'message': 'Bad Request'}), 400
    Comentarioagencia[id]['comentario'].append(comment)
    Comentarioagencia[id]['valoracion'].append(rating)
    return jsonify({'message': 'Comentario y valoración añadidas correctamente'}), 201
if id == '__main__':
    app.run()
"""
