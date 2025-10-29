# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = "Indefinido (no se puede dividir por cero)"
    else:
        division = a / b
    
    return (suma, resta, multiplicacion, division)

# Ejemplo de uso
num1 = 10   
num2 = 5
resultados = operaciones_basicas(num1, num2)

print("Resultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

