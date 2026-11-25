#media, mediana y moda

ventas = [10,7,4,6,8,10,10,9]

print(ventas)

total = sum(ventas)
cantidad = len(ventas)
promedio = total / cantidad
ordenadas = sorted(ventas)
mediana = (ordenadas[3] + ordenadas[4]) /2



print("Total vendido: ", total)
print("Cantidad de días: ", cantidad)
print("Promedio diario: ", promedio)
print("Ordenadas: ", ordenadas)
print("Mediana: ", mediana)



print(ventas)
print(ordenadas)




