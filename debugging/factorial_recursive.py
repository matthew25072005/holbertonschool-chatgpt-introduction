#!/usr/bin/python3
import sys

# Definimos una función recursiva para calcular el factorial de un número
def factorial(n):
    # Caso base: el factorial de 0 es 1
    if n == 0:
        return 1
    else:
        # Caso recursivo: n * factorial de (n-1)
        return n * factorial(n-1)

# Convertimos el primer argumento de la línea de comandos a un entero y calculamos su factorial
f = factorial(int(sys.argv[1]))

# Imprimimos el resultado del factorial
print(f)
