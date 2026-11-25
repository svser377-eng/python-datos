#conjuntos

canales = {"Instagram", "Facebook", "Tiktok"}

print(canales)

#agregar un canal
canales.add("LinkedIN")
canales.add("WhatsApp")

print(canales)

#comprobar si un elemento esta en el conjunto

print("Instagram" in canales)
print("WatsApp" in canales)


#unir conjuntos

campania_a = {"Instagram", "Facebook", "TikTok"}
campania_b = {"LinkedIN", "Youtube", "TikTok"}

print("\n Union: ")
campania_c = campania_a | campania_b  #union
print(campania_c)

print("\n Intersección: ")

campania_d = campania_a & campania_b # interseccion
print(campania_d)

print("\n Diferencia: ")

campania_e = campania_a - campania_b # interseccion
print(campania_e)



