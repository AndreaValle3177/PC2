def perfecto(n):
    suma_divisores = 0
    
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    
    return suma_divisores == n

numeros_perfectos = []

for num in range(1, 1000):
    if perfecto(num):  
        numeros_perfectos.append(num)

# Imprimir la lista correcta
print("Números perfectos:", numeros_perfectos)