# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    
    if numero < 0:
        print("Ingrese un número mayor o igual a 0.")
        return
    
    print(f"Serie de Fibonacci hasta la posición {numero}:")
    for i in range(numero + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    main()
