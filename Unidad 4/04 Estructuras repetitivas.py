# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

userInput = int(input("Ingrese un numero entero: "))

largo = len(str(userInput))

print(f"El {userInput} tiene {largo} cantidad de digitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

userInput1 = int(input("Ingrese el primer valor: "))

userInput2 = int(input("Ingrese el segundo valor: "))

suma = 0

if userInput1 == userInput2:
    print("Los valores son iguales!")
else:
    for i in range(min(userInput1, userInput2) + 1, max(userInput1, userInput2)):
        suma += i

    print(f"La suma entre los valores: {userInput1} y {userInput2} (sin incluirlos) es de: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0

while True:
    numero = int(input("Ingrese un numero entero (0 para terminar): "))
    
    if numero == 0:
        break
    total += numero

print(f"La suma total es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)

intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

    if intento == numero_secreto:
        adivinado = True
        print(f" Correcto! El numero era {numero_secreto}.")
        print(f"Lo hiciste en {intentos} intentos.")
    else:
        print("Incorrecto, de nuevo!")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

n = int(input("Ingrese un numero entero positivo: "))

suma = 0

for i in range(1, n + 1):
    suma += i

print(f"La suma de los numeros entre 0 y {n} es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

N = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(N):
    num = int(input(f"Ingrese el número {i+1}: "))

    # Par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo o negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1


print("\nResultados:")
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

N = 100

suma = 0

for i in range(N):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / N   # promedio

print(f"\nLa media de los {N} numeros ingresados es: {media}")


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ")


invertido = numero[::-1]

print(f"El numero invertido es: {invertido}")
