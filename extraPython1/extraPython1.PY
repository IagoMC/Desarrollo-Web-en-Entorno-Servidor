import random
arma=""
t=0
arma2=''

cont=0
e1=0
e2=0
while cont<5:
    print('Tu: '+str(e1)+'  Maquina: '+str(e2))   
    while t==0:
        arma=input('Piedra | Papel | Tijera  :' )
        if arma=='Piedra':
            t=1
        elif arma=='Papel':
            t=1
        elif arma=='Tijera':
            t=1

    t=0
    nr=random.randint(1,3)
    if nr==1:
        arma2="Piedra"
    elif nr==2:
        arma2="Papel"
    else:
        arma2="Tijera"


    if arma==arma2:
        print('EMPATE')
    elif arma=='Piedra' and arma2=='Tijera':
        print('Ronda ganada')
        print(arma+' Gana a '+arma2)
        e1=e1+1
        cont=cont+1

    elif arma=='Papel' and arma2=='Piedra':
        print('Ronda ganada')
        print(arma+' Gana a '+arma2)

        e1=e1+1
        cont=cont+1

    elif arma=='Tijera' and arma2=='Papel':
        print('Ronda ganada')
        print(arma+' Gana a '+arma2)
        e1=e1+1
        cont=cont+1    

    #
    
    elif arma2=='Piedra' and arma=='Tijera':
        print('Ronda Perdedor')
        print(arma2+' Gana a '+arma)
        e2=e2+1
        cont=cont+1

    elif arma2=='Papel' and arma=='Piedra':
        print('Ronda Perdedor')
        print(arma2+' Gana a '+arma)

        e2=e2+1
        cont=cont+1

    elif arma2=='Tijera' and arma=='Papel':
        print('Ronda Perdedor')
        print(arma2+' Gana a '+arma)
        e2=e2+1
        cont=cont+1  


if e1>e2 :
    print('')
    print('Tu: '+str(e1)+'  Maquina: '+str(e2))   
    print('GANADOR')        
else: 
    print('')
    print('Tu: '+str(e1)+'  Maquina: '+str(e2))   
    print('Perdedor')