#condicional IF
"""
SI se_ccumple_esta_condición:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro tipo de instrucciones
    
if condicion:
    instrucciones
else:
    otras instrucciones
    
#Operadores de comparación == igual
!= diferente
> mayor que
< menor que
<= menor o igual que
> mayor o igual que 


    """
# Ejemplo 1
print("########Ejemplo 1########")

# Color = "verde"
color = input("Adivina cual es mi color favorito: ")

color = "rojo"

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# Ejemplo 2
print("###########Ejemplo2 #############")
#year= 2020
#year=  int(input("¿En que año estamos?"))

if year >=2021:
    print("\nEstamos de 2019 en adelante!!")
else:
    print("Es una año anterior a 2021")
    

print("\n###########Ejemplo3 #############")

nombre="Raquel Rivas"
ciudad="Barcelona"
continente="Europa"
edad= 48
mayoria_edad=18

if edad >=mayoria_edad:
    print(f"{nombre}Es mayor de edad!!")
    if continente!="Europa":
        
    print("El usuario no es Europeo")
    else:
    print(f"Es europeo y de {ciudad} ")
    
else:
    print(f"{nombre} No es mayor de edad")