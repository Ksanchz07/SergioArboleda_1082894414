# Tablas de multiplicar del 1 al 10 usando for anidado

for numero in range(1, 11):
    print(f"\n--- Tabla de multiplicar del {numero} ---")
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
