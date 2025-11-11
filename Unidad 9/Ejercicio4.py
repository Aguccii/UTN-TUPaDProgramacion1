# Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.


def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
def main():
    numero = int(input("Ingrese un número entero positivo: "))
    
    if numero < 0:
        print("Ingrese un número mayor o igual a 0.")
        return
    
    binario = decimal_a_binario(numero)
    print(f"La representación binaria de {numero} es: {binario}")

if __name__ == "__main__":
    main()
    
