numeroU2=int(input('Introduce un numero '))
 

def func_factorial2 (numero):
    final=numero 
    if numero == 0:
        final=1
        return final
    else:
     for i in range(numero):
          if i==0:
              print("")
          else:
           final=final*(numero -i)

    return final


print(func_factorial2(numeroU2))