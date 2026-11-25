# Sesion 4
# Consultar cadenas de texto


producto ="memoria ram 16GB"

print(producto [0]) #p
print(producto [1]) #y
print(producto [2]) #t
print(producto [3]) #h
print(producto [4]) #o
print(producto [5]) #n
print(producto [6]) #1
print(producto [7]) #1

#f strings construir mensajes con variables

print(f"el producto es: {producto}")

# POSICIONES NEGATIVAS Y POSITIVAS

print(producto[6])
print(producto[-1])
print(producto[0])
print(len(producto))


# Extraer partes de una cadena de texto


print(producto[0:3])
print(producto[3:5])
print(producto[0:-1])

#longitud de una cadena de texto


longitud = len(producto)
print("la longitud de la cadena de texto es:", longitud)


# Metodos de cadenas de texto

#convertir a mayusculas
print(producto.upper())

#convertir a minusculas
print(producto.lower())

#capitalizar la primera letra de la cadena de texto
print(producto.capitalize())


#reemplazar un caracter por otro
print(producto.replace("a","e"))

#agregar una letra al final de la cadena de texto
print(producto+ " s")

#eliminar espacios en blanco al inicio y al final de la cadena de texto
print(producto.strip())

print("Limpiar Nombre")

#limpiar base
nombre = "     LUIS CARLOS VIVAS CARDENAS       "
print(f"El nombre del cliente es:{nombre.strip().title()}")
