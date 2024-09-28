def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

suma_primos = 0

for num in range(2, 100):
    if primo(num):
        suma_primos += num

# Mostrar el resultado
print("suma de primos", suma_primos)