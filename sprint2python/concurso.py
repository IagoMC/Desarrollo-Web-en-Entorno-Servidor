
print("Seleccione la respuesta correcta")
print("¿Cual es el mejor equipo?")

print("A - Barcelona")
print("B - Real Madrid")
print("C - Depor")
puntacion=0
respuesta=input()

if respuesta=="A":  
    puntacion=puntacion+10

elif respuesta=="a":
    puntacion=puntacion+10

elif respuesta=="Barcelona":
    puntacion=puntacion+10

else:
    puntacion=puntacion-5


print("Seleccione la respuesta correcta")
print("¿Cuanto es 2+2?")

print("A - 3")
print("B - 1")
print("C - 4")
respuesta2=input()

if respuesta2==4:  
    puntacion=puntacion+10

elif respuesta2=="C":    
    puntacion=puntacion+10
elif respuesta2=="c":    
    puntacion=puntacion+10
else:
    puntacion=puntacion-5



print("Seleccione la respuesta correcta")
print("¿Cuanto es 5+5?")

print("A - 9")
print("B - 10")
print("C - 6")
respuesta3=input()

if respuesta3==10:  
    puntacion=puntacion+10
elif respuesta3=="B":
    puntacion=puntacion+10
elif respuesta3=="b":
    puntacion=puntacion+10    
else:
    puntacion=puntacion-5


print('Puntacion') 
print (puntacion)
