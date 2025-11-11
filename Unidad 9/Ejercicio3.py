#  Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 ∧ 𝑚 = 𝑛 ∗ 𝑛 ∧ (𝑚−1) 
# Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
def main():
    base = float(input("Ingrese la base (número positivo): "))
    exponente = int(input("Ingrese el exponente (número positivo): "))
    
    if exponente < 0:
        print("Ingrese un exponente mayor o igual a 0.")
        return
    
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a {resultado}")

if __name__ == "__main__":
    main()


