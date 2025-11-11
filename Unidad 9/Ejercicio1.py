# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    
    if numero < 1:
        print("Ingrese un número mayor o igual a 1.")
        return
    
    print(f"Factoriales de 1 a {numero}:")
    for i in range(1, numero + 1):
        print(f"{i}! = {factorial(i)}")

if __name__ == "__main__":
    main()

