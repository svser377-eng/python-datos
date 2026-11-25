# programa en Python que permita registrar y mostrar la información de una actividad formativa, utilizando diferentes tipos de datos


print("Bienvenido a la Institución Educativa")

actividad = str(input("Ingrese la actividad: "))
cupos = int(input("Ingrese el # de cupos disponibles: "))
duracion_horas = float(input("Ingrese la duración de la actividad: "))

respuesta = input("Escriba -Y- si requiere inscripción ó -N- si no requiere inscripción:  ")

requiere_inscripcion = (respuesta == 'Y' )

print ("Actividad: ", actividad)
print(type(actividad))
print("# de cupos disponibles: ", cupos)
print(type(cupos))
print("Duración (horas): ", duracion_horas)
print(type(duracion_horas))
print("Requiere Inscripción?: ", requiere_inscripcion)
print(type(requiere_inscripcion))

