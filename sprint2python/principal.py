from factorial import func_factorial
from factorial2 import func_factorial2
import time
op=5
while op>2 or op==0 :
    print('1)- Factorial con recursiva')
    print('2)- Factorial sin recursiva')

    op=int(input('Introduce una opcion '))
    
print(op)

if op==1:
        start_time = time.time()
        numeroU=int(input('Introduce un numero '))
        func_factorial(numeroU)
        print(func_factorial(numeroU))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')


else:
    start_time = time.time()
    numeroU=int(input('Introduce un numero '))
    func_factorial2(numeroU)
    print(func_factorial2(numeroU))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')