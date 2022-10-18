import random
puntacion=0
v=0
r1=0
r2=0
r3=0
while v<3:
    nr=random.randint(1,3)
    if nr==1:
        r1=r1+1
    elif nr==2:
        r2=r2+1
    else :
        r3=r3+1

    if nr == 1 and r1!=2:
            v=v+1
            print("Seleccione la respuesta correcta")
            print("¿Cual es el mejor equipo? (A, B, C)")
            print("A - Barcelona")
            print("B - Real Madrid")
            print("C - Depor")
            respuesta=input()
            if respuesta=="A":  
                puntacion=puntacion+10
            elif respuesta=="a":
                puntacion=puntacion+10
            elif respuesta=="Barcelona":
                puntacion=puntacion+10
            else:
                puntacion=puntacion-5



    elif nr == 2  and r2!=2:
            v=v+1
            print("Seleccione la respuesta correcta")
            print("¿Cuanto es 2+2? (A, B, C)")

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
    elif nr==3  and r3!=2 :
            v=v+1
            print("Seleccione la respuesta correcta")
            print("¿Cuanto es 5+5? (A, B, C)")

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
