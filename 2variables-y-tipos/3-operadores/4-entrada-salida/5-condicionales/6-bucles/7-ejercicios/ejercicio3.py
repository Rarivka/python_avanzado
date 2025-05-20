"""
Ejercicio 3 escribir un programa que muestre los cuadrados (un número multiplicado por sí mismo)
delos 60 primeros números naturales. Resolverlo con for y con while
"""
# While

contador= 0
while contador <= 60:
    cuadrado = contador * contador
    print(f" El cuadrado de {contador}es {cuadrado}")
    contador += 1