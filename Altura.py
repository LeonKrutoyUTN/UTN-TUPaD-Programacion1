# Programa que calcula el Índice de Masa Corporal (IMC)
# Fórmula: IMC = peso (kg) / altura (m)^2

# Pedir al usuario peso y altura
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

# Validar que los valores sean positivos
if peso <= 0 or altura <= 0:
    print("Error: El peso y la altura deben ser mayores que 0.")
else:
    # Calcular el IMC
    imc = peso / (altura ** 2)
    
    # Mostrar el resultado explicando la fórmula
    print(f"IMC = {peso} / ({altura}^2) = {imc:.2f}")



