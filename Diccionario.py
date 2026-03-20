persona = {"nombre": "Keiner", "edad": 18, "ciudad": "Santa Marta"}

for clave in persona:
    print(clave)  # Imprime las claves del diccionario

for clave, valor in persona.items():
    print(clave + ": " + str(valor))