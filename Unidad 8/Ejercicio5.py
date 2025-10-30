# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error

with open("productos.txt", "r") as archivo:
    busqueda_Producto = input("Ingrese el nombre del producto a buscar: ")
    productos = []
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)
        
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == busqueda_Producto.lower():
            print(f"Producto encontrado: {producto}")
            encontrado = True
            break
    if not encontrado:
        print("Error: Producto no encontrado.")