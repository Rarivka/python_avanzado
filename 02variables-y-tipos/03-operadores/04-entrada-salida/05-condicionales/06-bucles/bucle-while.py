""""
# BUCLE WHILE 
Estructura de control que itera o repite la ejecución de una serie de instrucciones tantas veces como sea necesario ,hasta que deje de cumplirse la condición.

While condición: 
      bloque de instrucciones
      actualización de contador

"""
# Primer bucle: Imprimir números del 1 al 100
contador = 1
while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1
    print("----------------------")

# Segundo bucle: Concatenar números en una cadena
contador = 1
muestrame = "0"
while contador <= 100:
    muestrame = muestrame + "," + str(contador)
    contador += 1
print(muestrame)  # Imprimir solo al final

# Tabla de multiplicar
numero_usuario = int(input("¿De qué número quieres la tabla?: "))
if numero_usuario < 1:
    numero_usuario = 1

print(f"##### Tabla del {numero_usuario} ####")
contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
print("Tabla terminada.")