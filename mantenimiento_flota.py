#Programa de control de mantenimiento preventivo de flota
# por Luis Vivas para la clase del curso analísis de datos en Python 


flotas = [
      {"V-101": "320"},
      {"V-102": "780"},
      {"V-103": "1250"},
      {"V-104": "1680"},
      {"V-105": "450"},
      {"V-106": "920"},
      {"V-107": "1420"},
      {"V-108": "1850"},
      {"V-109": "610"},
      {"V-110": "1100"},
      {"V-111": "250"},
      {"V-112": "1550"}
]

kms = []

uso_reciente = 0
seguimiento = 0
programar_revision = 0
prioridad_alta = 0

def procesar_vehiculo():
    print("Procesar cada vehículo de la lista")
    for vehiculo in flotas:
        for j in vehiculo.items():
            print(j)

def recorrer_registros():
    if not kms:
        for vehiculo in flotas:
            for i in vehiculo.values():
                kms.append(int(i))
                print(i)
        print("Lista KMS cargada")
        print("valores recorridos")
    else:
          print("Lista Llena")

def obtener_categoria():
 global uso_reciente, seguimiento, programar_revision, prioridad_alta        
    # Usar acumuladores 
 for cont in kms:
    if 1 <= cont <= 499:
        uso_reciente +=1
    elif 500 <= cont <= 999:
        seguimiento +=1
    elif 1000 <= cont <= 1499:
        programar_revision +=1
    elif 1500 <= cont <= 1999:
        prioridad_alta +=1
 print("Categoría Asignada")

def mostrar_resultados():
    print("Resultados")
    print("Uso reciente:",uso_reciente)
    print("Seguimiento: ",seguimiento)
    print("Programar Revisión: ",programar_revision)
    print("Prioridad Alta: ",prioridad_alta)

def mostrar_detalles():
    for vehiculo in flotas:
        for codigo, valor in vehiculo.items():
            km = int(valor)
            
            if 1 <= km <= 499:
                categoria = "Uso reciente"
            elif 500 <= km <= 999:
                categoria = "Seguimiento"
            elif 1000 <= km <= 1499:
                categoria = "Programar Revisión"
            elif 1500 <= km <= 1999:
                categoria = "Prioridad Alta"
                
            print(f"Código: {codigo} | Kilometraje: {km} | Categoría: {categoria} |")

def calculos():
        print("lista de Kilometros:")
        print(kms)
        cantidad = len(kms)
        print("Cantidad Vehículos: ",cantidad)
        total = sum(kms)
        print("Total de Kilometros: ",total)
        promedio = total / cantidad
        print("Promedio de Kilometros: ",promedio)
        
        #mediana = (ordenadas[3] + ordenadas[4]) /2

def limpiar_cont():
    global uso_reciente, seguimiento, programar_revision, prioridad_alta
    uso_reciente =0
    seguimiento =0
    programar_revision =0
    prioridad_alta =0
    print("Contador Borrado") 

def consultar_vehiculo():
    codigo_buscado = input("Ingresa Codigo: ").strip().upper()

    for vehiculo in flotas:
            for codigo, valor in vehiculo.items():
                if codigo == codigo_buscado:
                    km = int(valor)

                    if 1 <= km <= 499:
                     categoria = "Uso reciente"
                    elif 500 <= km <= 999:
                        categoria = "Seguimiento"
                    elif 1000 <= km <= 1499:
                        categoria = "Programar Revisión"
                    elif 1500 <= km <= 1999:
                        categoria = "Prioridad Alta"
                    
                    print(f"Código: {codigo} | Kilometraje: {km} | Categoría: {categoria} |")
                    return
    print("Codigo no encontrado")            

#Menu de Opciones para el mantenimiento de la flota
while True:
     print("\n  ░░░░░░░░ SISTEMA MANTENIMIENTO FLOTA ░░░░░░░░ ")
     
     print("1 Procesar Vehiculos")
     print("2 Recorrer Registros y llenar Lista KMS")
     print("3 Asignar Categoría")
     print("4 Mostrar Resultados x Categoría")
     print("5 Mostrar Detalles de Vehiculos")
     print("6 Calculos")
     print("7 Limpiar Lista Contador Cat.")
     print("8 Consultar estado de Vehículo")
     print("9 Salir")
#     pendiente hacer calculos y presentar reporte

     opcion = input("\nSeleccione una opción: ")

     if  opcion == "1":
          procesar_vehiculo()
     elif opcion == "2":
          recorrer_registros()
     elif opcion == "3":
         obtener_categoria()
     elif opcion == "4":
         mostrar_resultados()
     elif opcion == "5":
         mostrar_detalles()
     elif opcion == "6": 
         calculos()
     elif opcion == "7":
         limpiar_cont()
     elif opcion == "8":
         consultar_vehiculo()
     elif opcion == "9":
         print("Vuelva Pronto!")
         break
     else:
         print("Opción incorrecta. Intente nuevamente.")