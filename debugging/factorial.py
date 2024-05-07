#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Error: El número debe ser no negativo"
    elif not isinstance(n, int):
        return "Error: El número debe ser un entero"
    else:
        result = 1
        while n > 1:
            result *= n
            n = n - 1
        return result

if len(sys.argv) > 1:
    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Error: El argumento debe ser un número entero")
else:
    print("Error: Debe proporcionar un argumento al ejecutar el script")