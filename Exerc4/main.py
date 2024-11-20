from meu_pacote.verificar_par import verificar_par
from meu_pacote.multiplicar import multiplicar
from meu_pacote.subtrair import subtrair

def main():
    numero = int(input("Digite um número para verificar se é par: "))
    if verificar_par(numero):
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")


    a = int(input("Digite o primeiro número da multiplicação: "))
    b = int(input("Digite o segundo número da multiplicação: "))
    print(f"O resultado de {a} * {b} é: {multiplicar(a, b)}")


    x = int(input("Digite o primeiro número para a subtração: "))
    y = int(input("Digite o segundo número para a subtração: "))
    print(f"O resultado de {x} - {y} é: {subtrair(x, y)}")


if __name__ == "__main__":
    main()            