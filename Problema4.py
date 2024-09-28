alumnos = []

while True:
    alumno = input("Ingrese nombre de alumno: ")
    
    notas = []
    for i in range(3):
        nota = int(input(f"Ingrese la nota {i+1} del alumno {alumno}: "))
        notas.append(nota)
    
    lista = {alumno: notas}
    
    alumnos.append(lista)
    
    continuar = input("¿Desea ingresar otro alumno? (Si/No): ").strip().lower()
    if continuar == 'no':
        break

print("Listado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(alumno)