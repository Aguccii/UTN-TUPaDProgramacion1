# Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = input("Ingrese el precio del nuevo producto: ")
nuevo_cantidad = input("Ingrese la cantidad del nuevo producto: ")

with open("productos.txt", "a") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n")
    
print("Nuevo producto agregado exitosamente.")
