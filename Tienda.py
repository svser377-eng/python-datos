# Programa de tienda que necesita registrar productos, cantidades y precios
print("Bienvenido a la tienda")
producto = " "
cantidad = 0
precio = 0.0
producto = input ("Por favor ingrese el producto: ")  
print ("Su producto es:", producto)
cantidad = input ("Por favor ingrese la cantidad: ")  
precio = input ("Por favor ingrese el precio unitario: ")
total = float (precio) * int(cantidad)
print("/*/*/*/*/*/*/*/*/* Resumen de tu compra /*/*/*/*/*/*/*/*/*/*")
print("\nProducto: \n",producto +"\nCantidad: \n",cantidad +"\nPrecio C/u: \n",precio +"\nTotal: \n",total)