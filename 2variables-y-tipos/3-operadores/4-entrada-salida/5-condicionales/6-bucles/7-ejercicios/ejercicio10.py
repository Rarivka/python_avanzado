"""
Ejercicio 10 El programa tiene que pedir la nota de 15 alumnos y sacer por pantalla cuantos han aprobadomy cuantos han suuspendido
"""
contador=0
aprobados=0
suspendidos=0

numero_alumnos=int(input("¿Cuántos alumnos tienes?:"))

while contador<=numero_alumnos:
    nota=int(input("¿Qué nota quieres ponerle al \"alumno{contador}\ "))
    if nota>=5:
        aprobados+=1
    else:
        suspendidos+=1
        
        
    contador+=1
    print(f"Alumnos aprobados:{aprobados}")
    print(f"Alumnos suspensos:{suspendidos}")
