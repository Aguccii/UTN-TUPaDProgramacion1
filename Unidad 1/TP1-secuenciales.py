# TP 1 Secuenciales - UTN
# Alumno: [Tu Nombre]
# Fecha: [Fecha de entrega]

# 1) Hola Mundo
print("Hola Mundo!")

# 2) Saludo con nombre
nombre = input("\nIngrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Datos personales
nombre = input("\nIngrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4) Área y perímetro de un círculo
import math
radio = float(input("\nIngrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

# 5) Segundos a horas
segundos = int(input("\nIngrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas.")

# 6) Tabla de multiplicar
numero = int(input("\nIngrese un número para mostrar su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Operaciones con dos números
num1 = int(input("\nIngrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# 8) Índice de masa corporal
altura = float(input("\nIngrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")

# 9) Celsius a Fahrenheit
celsius = float(input("\nIngrese la temperatura en grados Celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}°F")

# 10) Promedio de tres números
num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")




