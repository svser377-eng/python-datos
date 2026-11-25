producto_1 = {"codigo": "P001", "nombre": "Cuaderno", "precio": 4500}
producto_2 = {"codigo": "P002", "nombre": "Mouse", "precio": 35000}
producto_3 = {"codigo": "P003", "nombre": "Laptop", "precio": 4000000}

inventario = [producto_1, producto_2, producto_3]

print("Primer producto: ", inventario[0]["nombre"])
print("Segundo producto: ", inventario[1]["precio"])
print("Tercer producto: ", inventario[2]["precio"])

print("/*/*/*/*/*/*/*/*/*/*")

inventario[0]["precio"] = 5000
print("Nuevo precio:", inventario[0]["precio"])

print("Nuevo producto", inventario[2])