"""
Ejercicio 8 .¿Cuánto es el X por ciento de X número?
                           20% de 150

"""
numero1= int(input("Introduce el número: "))
porcentaje= int(input (f"¿Qué porcentaje quieres sacar de {numero1}"))

operación=(numero1*(porcentaje/100))

print(f"El {porcentaje}% {numero1}es:{operación}")