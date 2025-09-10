
#Trabajo Práctino Nº 3 - Estructuras condicionales




#1 Pedir la edad al usuario
edad = int(input("Ingresa tu edad: "))

# Verificar si es mayor de edad
if edad > 18:
    print("Es mayor de edad")



#2 Pedir la nota al usuario
nota = int(input("Ingresa tu nota: "))

# Verificar si aprueba o desaprueba
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")



#3 Solicita al usuario ingresar un número entero
numero = int(input("Ingrese un número: "))

# Usa el operador módulo para verificar si es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#4 Solicita la edad al usuario
edad = int(input("Ingrese su edad: "))

# Evalúa y muestra la categoría correspondiente
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")


#5 Solicita la contraseña al usuario
contrasena = input("Ingrese una contraseña: ")

# Verifica si la longitud está entre 8 y 14 caracteres
if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#6 Estadísticas:


import random
from statistics import mode, median, mean

# Genera la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcula los parámetros estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista generada:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Determina el sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo según los valores calculados.")


#7 Escribir un programa que solicite una frase

# Solicita una frase o palabra al usuario
texto = input("Ingrese una frase o palabra: ")

# Verifica si termina con una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"
    
# Imprime el resultado
print(texto)


#8 

# Solicita el nombre y la opción al usuario
nombre = input("Ingrese su nombre: ")
print("Elija una opción:")
print("1. Mostrar el nombre en mayúsculas")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra mayúscula")
opcion = input("Ingrese 1, 2 o 3: ")

# Aplica el formato solicitado
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida")

    
#9 TERREMOTO

# Solicita la magnitud al usuario
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasifica la magnitud según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")


#10 ESTACION SEGÚN EL HEMISFERIO

# Solicita datos al usuario
hemisferio = input("Ingrese el hemisferio (N para norte, S para sur): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

# Convierte el mes y día en un valor comparable (mmdd)
fecha = mes * 100 + dia

# Define las estaciones según el hemisferio
if hemisferio == "N":
    if (fecha >= 1221 and fecha <= 1231) or (fecha >= 101 and fecha <= 320):
        estacion = "Invierno"
    elif fecha >= 321 and fecha <= 620:
        estacion = "Primavera"
    elif fecha >= 621 and fecha <= 920:
        estacion = "Verano"
    elif fecha >= 921 and fecha <= 1220:
        estacion = "Otoño"
    else:
        estacion = "Fecha inválida"
elif hemisferio == "S":
    if (fecha >= 1221 and fecha <= 1231) or (fecha >= 101 and fecha <= 320):
        estacion = "Verano"
    elif fecha >= 321 and fecha <= 620:
        estacion = "Otoño"
    elif fecha >= 621 and fecha <= 920:
        estacion = "Invierno"
    elif fecha >= 921 and fecha <= 1220:
        estacion = "Primavera"
    else:
        estacion = "Fecha inválida"
else:
    estacion = "Hemisferio inválido"

# Imprime el resultado
print("Estación:", estacion)



#Vladimir Krutoy 
#Comisión: Ag25-1C-14 