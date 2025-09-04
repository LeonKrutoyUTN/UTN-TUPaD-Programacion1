# Programa que calcula el promedio de tres números

# Pedir los tres números al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Mostrar el resultado
print(f"El promedio de los números ingresados es: {promedio:.2f}")
