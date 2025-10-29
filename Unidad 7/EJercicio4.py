# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

guia = {}

for i in range(5):
    usuario = str(input("Ingrese un usuario a cargar: "))
    telefono = int(input("Ingrese su número telefónico: "))
    guia[usuario] = telefono

nombre_consulta = str(input("Ingrese el nombre del contacto que desea consultar: "))
if nombre_consulta in guia:
    print(f"El número telefónico de {nombre_consulta} es: {guia[nombre_consulta]}")
else:
    print("El contacto no existe en la guía telefónica.")


print(guia)
