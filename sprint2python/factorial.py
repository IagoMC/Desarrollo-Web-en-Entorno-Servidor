def func_factorial (numero):
    if (numero==1 or numero==0):
        return 1
    else:
        return (numero * func_factorial(numero-1))

