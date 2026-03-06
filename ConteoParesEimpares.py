# Programa que pide 10 números al usuario, cuenta pares e impares y muestra los contadores usando for con dos contadores

pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Ingresa el número {i+1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
