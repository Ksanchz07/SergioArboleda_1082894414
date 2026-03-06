# Programa que pide números al usuario hasta que escriba 0, suma todos y muestra la suma total usando while con acumulador

suma = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print(f"La suma total de los números ingresados es: {suma}")
