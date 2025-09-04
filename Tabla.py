# Programa que muestra la tabla de multiplicar de un número

# Pedir un número al usuario
numero = int(input("Ingresa un número: "))

# Imprimir la tabla de multiplicar del 1 al 10
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
