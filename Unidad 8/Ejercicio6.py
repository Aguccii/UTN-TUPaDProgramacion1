# Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.

productos = [
    {"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
    {"nombre": "Cuaderno", "precio": 450.0, "cantidad": 15},
    {"nombre": "Regla", "precio": 90.0, "cantidad": 20}
]

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado correctamente.")






