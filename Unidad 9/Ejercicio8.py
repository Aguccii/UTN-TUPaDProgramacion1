# Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
#  Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4 

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        contador = 1 if numero % 10 == digito else 0
        return contador + contar_digito(numero // 10, digito)
    
# Ejemplo
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))