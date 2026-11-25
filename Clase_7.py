#sesion-7


guias = ["G001","G002","G003","G004","G005","G006","G007"]

print("for")

for i in guias:
    print("Revisando envio", i)

#for +range

print("for + range")
for consecutivo in range(2):
    print("Revisando envío:", guias[consecutivo])

for consecutivo in range(2, 5):
    print("Revisando envio:", guias[consecutivo])



#contadores

contador = 0

for consecutivo in guias:
    contador +=1
    print("Revisando:", consecutivo)

print("Total:",contador)

#acumulador de kms
print("Acumuladores")

distancias =[15, 22, 10, 18]
distancia_total = 0

for distancia in distancias:
    distancia_total += distancia
print("Distancia total:", distancia_total)

#Contadores
print("Contadores")


  
envios = [
      {"estado": "entregado"},
      {"estado": "entregado"},
      {"estado": "devuelto"},
      {"estado": "ruta"},
      {"estado": "ruta"},
      {"estado": "ruta"},
      {"estado": "ruta"},
      {"estado": "ruta"},
      {"estado": "ruta"},
      {"estado": "ruta"}

]

entregados = 0
ruta = 0
devueltos = 0


for envio in envios:
    if envio["estado"] == "entregado":
        entregados += 1
    elif envio["estado"] == "ruta":
        ruta += 1
    else:
        devueltos +=1

# Mostrar Resultados

print("Resumen de Envios:")
print("Entregados:", entregados)
print("En Ruta:", ruta)
print("Devueltos:", devueltos)

#While

print("Intentos de entrega")

guia = "G001"

intentos = 0
entregado = False

while intentos < 3  and entregados == False:
    intentos +=1

    print ("guia", guia)
    print("intentos de entrega", intentos)

resultado = input("se entrego el paquete? (S/N):     ").lower()

if resultado == "s":
    entregado = True
else:
    nentregado = False

if entregado:
    print("Envio entregado")
else:
    print("Envio devuelto")

print ("total intentos:", intentos)


# frecuencias de entregas en el tiempo

tiempos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

grupo_1_3 = 0
grupo_4_6 = 0
grupo_7_9 = 0
grupo_10_12 = 0


for cont in tiempos:
    if 1 <= cont <=3:
        grupo_1_3 +=1
    elif 4 <= cont <=6:
        grupo_4_6 +=1
    elif 7 <= cont <=9:
        grupo_7_9 +=1
    elif 10 <= cont <=12:
        grupo_10_12 +=1



print("Reporte de tiempos de entrega")
print("de 1  a 3 días:",grupo_1_3, "entregas")
print("de 4  a 6 días:",grupo_4_6, "entregas")
print("de 7  a 9 días:",grupo_7_9, "entregas")
print("de 10  a 12 días:",grupo_10_12, "entregas")



