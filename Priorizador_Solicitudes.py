# Priorizador de Solicitudes

data_entrada = {
    "codigo":"ADM-004",
    "tipo":"Actualización de Datos",
    "area_solicitante":"Talento Humano",
    "dias_pendiente":"4",
    "afecta_operacion":False,
    "estado":"pendiente",
    
}
print("\n Estado:")
print(data_entrada.get("estado"))
print("\n Días Pendiente:")
print(data_entrada.get("dias_pendiente"))
print("\n Afecta la Operación:")
print(data_entrada.get("afecta_operacion"))



if data_entrada.get("estado") == "cerrada":
    print("CERRADA: No se requiere nueva gestión")

elif  data_entrada.get("afecta_operacion") == True and data_entrada.get("dias_pendiente") >= "2":
    print("URGENTE: Escalar al responsable para atención prioritaria")

elif data_entrada.get("afecta_operacion") == True or data_entrada.get("dias_pendiente") >= "5":
    print("PRIORITARIA: Programar atención preferente")

else:
    print("NORMAL: Mantener flujo habitual de atención")
