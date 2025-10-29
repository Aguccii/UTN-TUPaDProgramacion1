# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")

    nota1 = int(input(f"Ingrese la nota 1 de {nombre}: "))
    nota2 = int(input(f"Ingrese la nota 2 de {nombre}: "))
    nota3 = int(input(f"Ingrese la nota 3 de {nombre}: "))

    notas = (nota1, nota2, nota3)

    promedio = sum(notas) / len(notas)

    alumnos[nombre] = promedio

    print(f"El promedio de {nombre} es: {promedio:.2f}\n")

print("Promedios finales de los alumnos:")
for nombre, promedio in alumnos.items():
    print(f"{nombre}: {promedio:.2f}")













