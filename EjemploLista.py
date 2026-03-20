estudiantes=['Keiner', 'Juan', 'Camilo', 'Sergio', 'Juanes', 'Maria']

# Agregar un nuevo estudiante al final 
estudiantes.append('Marcos') 
print(estudiantes)
estudiantes.append('Edwin')
print(estudiantes)
estudiantes.append('Laura')
print(estudiantes)
estudiantes.append('Yarith ')   
print(estudiantes) 

print(len(estudiantes))  # Imprime la cantidad de estudiantes

if 'Maria' in estudiantes:
    print("Maria está en la lista de estudiantes.")

estudiantes.remove('Camilo')  # Elimina la primera ocurrencia de 'Camilo'
print(estudiantes)