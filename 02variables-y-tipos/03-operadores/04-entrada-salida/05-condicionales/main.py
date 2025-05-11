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

#Operadores lógicos
And=Y
Or= O
!=Negación
Not=No

    """
    # Ejemplo 1
print("\n######## Ejemplo 1 ########")

color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")

# Ejemplo 2
print("\n######## Ejemplo 2 ########")

year = int(input("¿En qué año estamos? "))

if year >= 2021:
    print("Estamos de 2021 en adelante!!")
else:
    print("Es un año anterior a 2021")

# Ejemplo 3
print("\n######## Ejemplo 3 ########")

nombre = "Raquel Rivas"
ciudad = "Barcelona"
continente = "Europa"
edad = 48
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad!!")
    if continente == "Europa":
        print(f"Es europeo y de {ciudad}")
    else:
        print("El usuario no es europeo")
else:
    print(f"{nombre} no es mayor de edad")
    
    # Ejemplo 4
    
print("\n ######## Ejemplo 4 ########")
dia= int(input("Introduce el número del día de la semana:"))
"""
if dia == 1:
   print("Es lunes")
else:
    if dia ==2:
       print("Es martes")
    else:
        if dia ==3:
            print("Es miércoles")
        
    
    """
    #Ejemplo 5 Elif
    # 
print("\n######## Ejemplo 5 ########")  

    
if dia==1:
       print("Es lunes")
elif dia==2:
        print("Es martes")
        
 #Ejemplo 6 Operadores lógicos múltiples condiciones
    # 
print("\n######## Ejemplo 6 ########")  
edad_minima=16
edad_maxima=64
edad_oficial= int(input("¿Tienes edad de trabajar:introduce tu edad"))
if edad>=16 and edad_oficial <=64:
    print("Está en edad de trabajar!!")
else:
    print("No está en edad de trabajar")

 #Ejemplo 7 
    # 
print("\n######## Ejemplo 7 ########")  
pais= "Alemania"

if pais== "Mexico" or pais== "España" or pais =="Colombia":
   print(f"{pais} es un pais de habla hispana!")
else:
     print(f"{pais} no es un país de habla hispana:")
    
#Ejemplo 8
    # 
print("\n######## Ejemplo 8 ########")  
pais="España"
if not (pais== "Mexico" or pais== "España" or pais =="Colombia"):
   print(f"{pais} No es un pais de habla hispana!")
else:
     print(f"{pais} Sí es un país de habla hispana:")
     
#Ejemplo 8
    # 
print("\n######## Ejemplo 8 ########")  
pais="Colombia"
if pais!= "Mexico" and pais== "España" and pais !="Colombia":
     print(f"{pais} No es un pais de habla hispana!")
else:
     print(f"{pais} Sí es un país de habla hispana:")