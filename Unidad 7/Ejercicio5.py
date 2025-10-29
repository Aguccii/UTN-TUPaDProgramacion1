# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

set_palabras = set(frase.split())
print("Palabras únicas:", set_palabras)

diccionario_palabras = {}
for conteo in frase.split():
    if conteo in diccionario_palabras:
        diccionario_palabras[conteo] += 1
    else:
        diccionario_palabras[conteo] = 1

print("Cantidad de veces que aparece cada palabra:", diccionario_palabras)
