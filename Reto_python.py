#Programa de registro de usuarios entrega de Medicamentos
# por Luis Vivas para la clase del curso analísis de datos en Python 

pacientes = []

def agregar_paciente():
    print("\n  ░░░░░░░░ SISTEMA ENTREGA DE MEDICAMENTOS ░░░░░░░░")
    documento = leer_entero_valido("\n Ingrese el # de documento del paciente: ")
    
    for paciente in pacientes:
        if paciente["documento"] == documento:
            print("El paciente ya existe en la lista")
            return

    nombre = input(" \n Ingrese el nombre del paciente: ")
    orden = leer_entero_valido("\n Ingrese el # de orden: ")
    direccion = input("\n Ingrese la dirección de entrega: ")
    telefono = input("\n Ingrese el # de teléfono: ")

    paciente = {
        "documento": documento,
        "nombre": nombre,
        "orden": orden,
        "direccion": direccion,
        "telefono": telefono
    }

    pacientes.append(paciente)
    print("Paciente registrado correctamente.")

def mostrar_pacientes():
    print("\n LISTA DE PACIENTES ")

    if not pacientes:
        print("No hay pacientes en la lista")
        return

    for i, paciente in enumerate(pacientes, 2):
        print(f"\nPaciente {i}")
        print(f"# de documento: {paciente['documento']}".strip())
        print(f"Nombre del paciente: {paciente['nombre']}".strip().title())
        print(f"#orden: {paciente['orden']}".strip())
        print(f"Dirección de entrega: {paciente['direccion']}".strip().title())
        print(f"Teléfono: {paciente['telefono']}".strip())

def consultar_paciente():
    documento = leer_entero_valido("\nIngrese el documento a consultar: ")

    for paciente in pacientes:
        if paciente["documento"] == documento:
            print("\n Paciente encontrado:")
            print(f"Nombre del paciente: {paciente['nombre']}".strip().title())
            print(f"# de orden: {paciente['orden']}")
            print(f"Dirección de entrega: {paciente['direccion']}".strip().title())
            print(f"Teléfono: {paciente['telefono']}")
            return

    print("Paciente no encontrado.")

def eliminar_paciente():
    documento = leer_entero_valido("\nIngrese el documento a eliminar: ")

    for paciente in pacientes:
        if paciente["documento"] == documento:
            pacientes.remove(paciente)
            print("Paciente eliminado correctamente.")
            return

    print("Paciente no encontrado.")

def comprobacion():
    if not pacientes:
            print("No hay pacientes en la lista")
            return
       
    print(len(pacientes)," Paciente(s) en la lista")

def leer_entero_valido(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Entrada no valida, ingrese solo # enteros")
            continue
        if valor <= 0:
         print("El numero debe ser mayor a 0")
         continue
        return valor

while True:
    print("\n  ░░░░░░░░ SISTEMA ENTREGA MEDICAMENTOS ░░░░░░░░ ")
    print("1 Agregar paciente")
    print("2 Mostrar lista de pacientes")
    print("3 Consultar paciente")
    print("4 Eliminar paciente")
    print("5 Salir")
    print("6 Comprobación")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        mostrar_pacientes()
    elif opcion == "3":
        consultar_paciente()
    elif opcion == "4":
        eliminar_paciente()
    elif opcion == "6":
        comprobacion()
    elif opcion == "5":
        print("Espere la entrega de medicamentos en su domicilio")
        break
    else:
        print("Opción incorrecta. Intente nuevamente.")



