# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

notas = [9.1, 8.5, 7.3, 6.0, 10.0, 4.5, 5.8, 9.7, 8.0, 7.5]

print("Notas de los estudiantes:", notas)

promedio = sum(notas) / len(notas)
print("Promedio de notas:", promedio)

nota_max = max(notas)
nota_min = min(notas)

print("Nota mas alta:", nota_max)
print("Nota mas baja:", nota_min)


# 2)Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista

productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

print("\n Lista de productos ordenada alfabéticamente:")
print(sorted(productos))

eliminar = input("\n Que producto desea eliminar de la lista? ")

if eliminar in productos:
    productos.remove(eliminar)
    print("\nProducto eliminado correctamente.")
else:
    print("\nEl producto no estaba en la lista.")

print("Lista actualizada:", productos)


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]

print("Lista original:", numeros)

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNumeros pares:", pares)
print("Cantidad de pares:", len(pares))

print("\nNumeros impares:", impares)
print("Cantidad de impares:", len(impares))

# 4) Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = list(set(datos))
print(sin_repetidos)

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "Marcos", "Lucia", "Pedro", "Sofia", "Juan", "Valeria"]

print("Lista inicial:", estudiantes)

accion = input("Desea agregar o eliminar un estudiante? (agregar/eliminar): ")

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no esta en la lista")

print("Lista final:", estudiantes)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [10, 20, 30, 40, 50, 60, 70]

rotada = [numeros[-1]] + numeros[:-1]

print("Lista original:", numeros)
print("Lista rotada:", rotada)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 25],
    [14, 28],
    [11, 24],
    [13, 27],
    [15, 30],
    [10, 22],
    [16, 29]
]

minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

amplitudes = [maximas[i] - minimas[i] for i in range(len(temperaturas))]
mayor_amplitud = max(amplitudes)
dia_mayor_amplitud = amplitudes.index(mayor_amplitud) + 1

print("Promedio minimas:", promedio_min)
print("Promedio maximas:", promedio_max)
print("Mayor amplitud termica en el dia:", dia_mayor_amplitud)

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [9, 5, 8],
    [6, 7, 7],
    [8, 9, 10],
    [5, 6, 4]
]

for i in range(len(notas)):
    promedio_est = sum(notas[i]) / len(notas[i])
    print("Promedio del estudiante", i+1, ":", promedio_est)

for j in range(len(notas[0])):
    promedio_mat = sum(notas[i][j] for i in range(len(notas))) / len(notas)
    print("Promedio de la materia", j+1, ":", promedio_mat)

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

turno = "X"

for _ in range(9):
    for fila in tablero:
        print(" ".join(fila))
    print()
    
    fila = int(input("Ingrese fila (0-2) para " + turno + ": "))
    col = int(input("Ingrese columna (0-2) para " + turno + ": "))
    
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada, intente de nuevo")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [5, 3, 4, 6, 2, 7, 3],   # producto 1
    [2, 6, 3, 5, 4, 8, 6],   # producto 2
    [7, 5, 6, 3, 5, 4, 2],   # producto 3
    [4, 4, 5, 7, 6, 5, 8]    # producto 4
]

for i in range(len(ventas)):
    total_producto = sum(ventas[i])
    print("Total vendido producto", i+1, ":", total_producto)

totales_dias = [sum(ventas[j][i] for j in range(len(ventas))) for i in range(len(ventas[0]))]
mayor_ventas_dia = max(totales_dias)
dia_mayor = totales_dias.index(mayor_ventas_dia) + 1

print("Dia con mayores ventas totales:", dia_mayor)

totales_productos = [sum(fila) for fila in ventas]
mas_vendido = max(totales_productos)
producto_mas_vendido = totales_productos.index(mas_vendido) + 1

print("Producto mas vendido en la semana:", producto_mas_vendido)



