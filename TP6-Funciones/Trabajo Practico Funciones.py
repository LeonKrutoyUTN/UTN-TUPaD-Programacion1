
#Práctico 2: Funciones en Python



#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()


#2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_usuario = input("Por favor, ingrese su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)


#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su residencia: ")

# Llamar a la función con los datos ingresados
informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)


#4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio_usuario = float(input("Ingrese el radio del círculo: "))

area = calcular_area_circulo(radio_usuario)
perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#5 
def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos_usuario = float(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos_usuario)
print(f"{segundos_usuario} segundos son equivalentes a {horas:.2f} horas.")


#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar número al usuario
n = int(input("Ingrese un número para imprimir su tabla de multiplicar: "))
# Llamar a la función con el número ingresado
tabla_multiplicar(n)


#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: división por cero"
    return suma, resta, multiplicacion, division

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso_usuario = float(input("Ingrese su peso en kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso_usuario, altura_usuario)
print(f"El índice de masa corporal (IMC) es: {imc:.2f}")


#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C es equivalente a {temp_fahrenheit:.2f}°F")


#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio de los tres números es: {promedio:.2f}")



#Vladimir Krutoy 
#Comisión: Ag25-1C-14 