# Programa que realiza operaciones con dos números enteros distintos de 0

# Pedir los dos números al usuario
num1 = int(input("Ingresa el primer número (distinto de 0): "))
num2 = int(input("Ingresa el segundo número (distinto de 0): "))

# Verificar que ninguno sea 0
if num1 == 0 or num2 == 0:
    print("Error: ambos números deben ser distintos de 0.")
else:
    # Realizar operaciones
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2

    # Mostrar resultados
    print(f"\nResultados con {num1} y {num2}:")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division:.2f}")
