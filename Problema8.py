def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0:
        return 1  
    return n * factorial(n - 1)  

try:
    numero = int(input("Ingrese un número entero no negativo: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError as e:
    print(e)