import math
from meu_modulo import saudacao, dobro
print(saudacao("Antônio"))
raiz_quadrada_numero = int(input("Digite um número para calcular a raiz quadrada: "))

def raiz_quadrada(numero):
    return print(f"Resultado da raiz quadrada de {numero} é = {math.sqrt(numero)}")
raiz_quadrada_resultado = raiz_quadrada(raiz_quadrada_numero)

resultado_dobro = dobro(5)
print(f"O dobro de 5 é: {resultado_dobro}")