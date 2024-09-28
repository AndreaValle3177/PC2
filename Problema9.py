usuario = input("Ingrese cadena de texto: ")

vocales_omitidas = "aeiouAEIOU"

texto_sin_vocales = ""
for char in usuario:
    if char not in vocales_omitidas:
        texto_sin_vocales += char

print("Texto sin vocales:", texto_sin_vocales)