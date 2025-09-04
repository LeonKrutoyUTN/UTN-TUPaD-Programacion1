# Programa que convierte grados Celsius a Fahrenheit

# Pedir la temperatura en Celsius al usuario
celsius = float(input("Ingresa la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# Mostrar el resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
