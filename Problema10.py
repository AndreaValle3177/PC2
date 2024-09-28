def convertir(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo",
        "Junio", "Julio", "Agosto", "Septiembre",
        "Octubre", "Noviembre", "Diciembre"
    ]
    
    if '/' in fecha: 
        mes, dia, año = fecha.split('/')
        mes = int(mes)  
    else: 
        parte, año = fecha.split(',')
        dia = parte.split()[1] 
        mes = meses.index(parte.split()[0]) + 1  
    
    return f"{int(año):04}-{mes:02}-{int(dia):02}"

fecha_usuario = input("Ingrese una fecha (mes/día/año o 'Mes día, año'): ")
fecha_convertida = convertir(fecha_usuario)
print("Fecha en formato AAAA-MM-DD:", fecha_convertida)