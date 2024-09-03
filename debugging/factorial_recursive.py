#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    try:
        # Verificar que se haya proporcionado un argumento
        if len(sys.argv) < 2:
            raise ValueError("Debe proporcionar un número como argumento.")
        
        # Convertir la entrada a entero
        n = int(sys.argv[1])
        
        # Verificar que el número no sea negativo
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        
        # Calcular y mostrar el factorial
        f = factorial(n)
        print(f)
    
    except ValueError as e:
        print(f"Error: {e}")
