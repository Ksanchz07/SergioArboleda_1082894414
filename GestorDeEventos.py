import datetime

def crear_evento(nombre, dia, mes, año):
    fecha = datetime.date(año, mes, dia)
    return {"nombre": nombre, "fecha": fecha}

def dias_hasta_evento(fecha_evento):
    hoy = datetime.date.today()
    diferencia = fecha_evento - hoy
    return diferencia.days

def evento_pasado(fecha_evento):
    hoy = datetime.date.today()
    return fecha_evento < hoy

def main():
    nombre = input("Ingrese el nombre del evento: ")
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    evento = crear_evento(nombre, dia, mes, año)
    fecha_evento = evento["fecha"]
    if evento_pasado(fecha_evento):
        dias = dias_hasta_evento(fecha_evento)
        print(f"El evento '{evento['nombre']}' ya pasó hace {-dias} días.")
    else:
        dias = dias_hasta_evento(fecha_evento)
        if dias == 0:
            print(f"El evento '{evento['nombre']}' es hoy.")
        else:
            print(f"Faltan {dias} días para el evento '{evento['nombre']}'.")

if __name__ == "__main__":
    main()