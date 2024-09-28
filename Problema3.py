numeros = []

while True:
    Usuario = input("¿Desea ingresar un número? (Si/No): ")
    if Usuario == 'si':
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)  
    elif Usuario == 'no':
        break
    else:
        print("Por favor, ingrese 'Si' o 'No'.")

pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)