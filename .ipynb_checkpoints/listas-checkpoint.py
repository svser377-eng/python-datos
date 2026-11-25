# Listas

lista = ["monitor" , "teclado" , "mouse" , "pendrive" ]


print(lista)
print(len(lista))


#agregar un elemento al final de la lista
lista.append("impresora")
print(lista)

#agregar un elemento en una posicion especifica de la lista
lista.insert(0,"disco duro")
print(lista)

#eliminar un elemento de la lista
lista.remove("pendrive")
print(lista)


#eliminar un elemento de la lista por posicion
del lista[2]
print(lista)

#ordenar lista por orden alfabetico
lista.sort()
print(lista)


#ordenar lista al contrario
lista.sort(reverse=True)
print(lista)


#unir dos listas
lista_2 = ["teclado inalambrico","mouse inalambrico","pendrive extraible","audifono inalambrico"]
lista_3 = lista + lista_2
print(lista_3)


#convertir cadena de texto a lista
cadena ="monitor,teclado,mouse,pendrive"
lista_4 = cadena.split(",")
print(lista_4)


#contar elementos de una lista
print(len(lista_4))
print(len(lista_3))
print(len(lista_2))
print(len(lista))