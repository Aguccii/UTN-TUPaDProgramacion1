# Armá un diccionario donde las keys sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.


tienda = {
    "manzanas": 50,
    "bananas": 30,
    "naranjas": 20
}

while True:

    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        producto = input("Ingresa el nombre del producto: ")
        stock = tienda.get(producto)
        if stock is None:
            print(f"El producto '{producto}' no existe en la tienda.")
        else:
            print(f"El stock de '{producto}' es: {stock} unidades.")
    
    elif opcion == "2":
        producto = input("Ingresa el nombre del producto: ")
        if producto not in tienda:
            print(f"El producto '{producto}' no existe en la tienda.")
        else:
            unidades = int(input(f"Ingresa la cantidad de unidades a agregar al stock de '{producto}': "))
            tienda[producto] += unidades
            print(f"Nuevo stock de '{producto}': {tienda[producto]} unidades.")

    elif opcion == "3":
        producto = input("Ingresa el nombre del nuevo producto: ")
        if producto in tienda:
            print(f"El producto '{producto}' ya existe en la tienda.")
        else:
            unidades = int(input(f"Ingresa la cantidad de unidades para '{producto}': "))
            tienda[producto] = unidades
            print(f"Producto '{producto}' agregado con un stock de {unidades} unidades.")
            
    elif opcion == "4":
        print("Saliendo del programa.")
        break


