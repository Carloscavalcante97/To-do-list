# Exceções são erros que podem ocorrer durante a execução de um programa.
# Elas podem ser tratadas para evitar que o programa pare de funcionar.

print("Exemplo de exceções em Python")
while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
    
    except ValueError:
        print("Você não digitou um número inteiro válido.")
    except ZeroDivisionError:
        print("Você não pode dividir por zero.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    else:
        print(f"Resultado: {resultado}")
        print("Fim do programa.") 
        break
        
    
