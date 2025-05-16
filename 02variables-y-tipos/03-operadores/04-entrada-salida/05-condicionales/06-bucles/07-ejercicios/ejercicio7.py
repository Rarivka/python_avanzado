"""
Ejercicio 7 Hacer un programa que muestre todos los números impares entre dos numeros que elija el usuario
"""
num1= int(input("Introduce un número:"))
num2= int(input("Introduce el siguiente número:"))

if num1<num2:
    
    for x in range (num1, (num2+1)):
        if x%2==0:
            print(f"{x}Es par")
        else:
            print(f"{x}No Es par")

else:
    print("El num1 debe ser mayor al 2")