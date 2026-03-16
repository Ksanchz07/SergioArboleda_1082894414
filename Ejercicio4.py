def validar_cedula(cedula):
    return cedula.isdigit() and 8 <= len(cedula) <= 10

def validar_email(email):
    partes = email.split('@')
    return len(partes) == 2 and '.' in partes[1]

def validar_calificaciones(calificaciones):
    return all(isinstance(c, (int, float)) and 0 <= c <= 5 for c in calificaciones)

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0.0
    return round(sum(calificaciones) / len(calificaciones), 2)

def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"

def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None
    promedio = calcular_promedio(calificaciones)
    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio
    }

def listar_estudiantes(lista_estudiantes):
    print("\nLista de Estudiantes:")
    print("Cédula\t\tNombre\t\tPromedio\tDesempeño")
    print("-" * 60)
    for est in lista_estudiantes:
        desempeño = clasificar_desempeño(est["promedio"])
        print(f"{est['cedula']}\t\t{est['nombre']}\t\t{est['promedio']}\t\t{desempeño}")

def main():
    estudiantes = []
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            cedula = input("Ingresa la cédula (8-10 dígitos): ")
            nombre = input("Ingresa el nombre: ")
            email = input("Ingresa el email: ")
            num_calif = int(input("Número de calificaciones: "))
            calificaciones = []
            for i in range(num_calif):
                calif = float(input(f"Ingresa calificación {i+1}: "))
                calificaciones.append(calif)
            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)
            if estudiante:
                estudiantes.append(estudiante)
                print("Estudiante agregado exitosamente.")
            else:
                print("Datos inválidos. No se pudo agregar el estudiante.")
        elif opcion == '2':
            listar_estudiantes(estudiantes)
        elif opcion == '3':
            cedula_buscar = input("Ingresa la cédula a buscar: ")
            encontrado = False
            for est in estudiantes:
                if est['cedula'] == cedula_buscar:
                    desempeño = clasificar_desempeño(est["promedio"])
                    print(f"Estudiante encontrado:")
                    print(f"Cédula: {est['cedula']}")
                    print(f"Nombre: {est['nombre']}")
                    print(f"Email: {est['email']}")
                    print(f"Promedio: {est['promedio']}")
                    print(f"Desempeño: {desempeño}")
                    encontrado = True
                    break
            if not encontrado:
                print("Estudiante no encontrado.")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
