numero = 1500  

while 1500 <= numero <= 2700: 
    numero = int(input("Introduzca un número: "))  
    if numero % 7 == 0 and numero % 5 == 0:
        print(f"{numero} es divisible por 7 y múltiplo de 5")
    else:
        print(f"{numero} no es divisible por 7 ni múltiplo de 5")