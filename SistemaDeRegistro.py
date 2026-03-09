# Sistema de registro de estudiantes
# Variables acumuladoras
suma_calificaciones = 0
mejor_nombre = ""
mejor_calificacion = 0
peor_nombre = ""
peor_calificacion = 6

# Ciclo para registrar 5 estudiantes
for i in range(1, 6):
    print("\n--- Estudiante " + str(i) + " ---")
    
    # Solicitar nombre
    nombre = input("Nombre: ")
    
    # Validar edad
    edad_valida = False
    while edad_valida == False:
        edad = int(input("Edad (5-100): "))
        if edad >= 5 and edad <= 100:
            edad_valida = True
        else:
            print("Edad invalida. Debe estar entre 5 y 100")
    
    # Validar calificacion
    calificacion_valida = False
    while calificacion_valida == False:
        calificacion = int(input("Calificacion (0-5): "))
        if calificacion >= 0 and calificacion <= 5:
            calificacion_valida = True
        else:
            print("Calificacion invalida. Debe estar entre 0 y 5")
    
    # Acumular calificaciones
    suma_calificaciones = suma_calificaciones + calificacion
    
    # Encontrar mejor calificacion
    if i == 1:
        mejor_nombre = nombre
        mejor_calificacion = calificacion
        peor_nombre = nombre
        peor_calificacion = calificacion
    else:
        if calificacion > mejor_calificacion:
            mejor_nombre = nombre
            mejor_calificacion = calificacion
        
        if calificacion < peor_calificacion:
            peor_nombre = nombre
            peor_calificacion = calificacion

# Calcular promedio
promedio = suma_calificaciones / 5

# Mostrar resultados
print("\n========== RESULTADOS ==========")
print("Mejor estudiante: " + mejor_nombre + " con " + str(mejor_calificacion))
print("Peor estudiante: " + peor_nombre + " con " + str(peor_calificacion))
print("Calificacion promedio: " + str(promedio))
