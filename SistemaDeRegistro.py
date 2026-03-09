# Programa de registro de estudiantes
# Se solicitan datos de 5 estudiantes y se realizan validaciones

NUM_ESTUDIANTES = 5

# Variables acumuladoras y de seguimiento
suma_calificaciones = 0.0
mejor_nombre = None
mejor_calificacion = -1.0
peor_nombre = None
peor_calificacion = 6.0  # fuera de rango para asegurar reemplazo

for i in range(1, NUM_ESTUDIANTES + 1):
    print(f"\n--- Estudiante {i} ---")
    # validación del nombre (no vacío)
    nombre = input("Nombre: ").strip()
    while nombre == "":
        nombre = input("Nombre no puede estar vacío. Ingrese nuevamente: ").strip()

    # validación de la edad
    while True:
        try:
            edad = int(input("Edad: "))
        except ValueError:
            print("Edad debe ser un número entero.")
            continue
        if 5 <= edad <= 100:
            break
        else:
            print("Edad inválida. Debe estar entre 5 y 100.")

    # validación de la calificación
    while True:
        try:
            calificacion = float(input("Calificación (0-5): "))
        except ValueError:
            print("Calificación debe ser un número.")
            continue
        if 0 <= calificacion <= 5:
            break
        else:
            print("Calificación inválida. Debe estar entre 0 y 5.")

    # actualizar acumuladores y comparaciones
    suma_calificaciones += calificacion
    if calificacion > mejor_calificacion:
        mejor_calificacion = calificacion
        mejor_nombre = nombre
    if calificacion < peor_calificacion:
        peor_calificacion = calificacion
        peor_nombre = nombre

# cálculo final
promedio = suma_calificaciones / NUM_ESTUDIANTES

print("\n=== Resultados ===")
print(f"Estudiante con la calificación más alta: {mejor_nombre} ({mejor_calificacion})")
print(f"Estudiante con la calificación más baja: {peor_nombre} ({peor_calificacion})")
print(f"Calificación promedio de todos: {promedio:.2f}")
