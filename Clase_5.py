#sesion 5


#diccionarios

televisores ={
    "marca": "Samsung",
    "precio": "5400000",
    "pulgadas": "50",
    "color":"negro",
    "resolucion": "4k",
}

print(televisores["marca"])
print(televisores["precio"])
print(televisores["pulgadas"])
print(televisores["color"])
print(televisores["resolucion"])


#corchetes mala consulta
print("/*/*/*/*/*/*/")

print(televisores.get("precio"))
print(televisores.get("disponible"))


print("/*/*/*/*/*/*/")

televisores["disponible"] = True

print("Existen televisores???")

print(televisores["disponible"])


print("/*/*/*/*/*/*/")

#modificar informacion
televisores["precio"] = 6000000
print(televisores)

#eliminar informacion
del televisores["disponible"]
print(televisores)

print("/*/*/*/*/*/*/*/*/*/*/*")
#consultar grupos de datos
print("\n",televisores.items())
print("\n",televisores.keys())
print("\n",televisores.values())

#coleccion de registros

electrodomesticos_cocina = [
    {
        "producto": "microondas",
        "marca": "LG",
        "litro": "22",
        "color":"negro",
        "disponible": True,
    },
    {
        "producto": "sanduchera",
        "marca": "Oster",
        "color": "negro",
        "disponible": True,
        
    }
]

print(electrodomesticos_cocina[0]['marca'])
print(electrodomesticos_cocina[1]["marca"])