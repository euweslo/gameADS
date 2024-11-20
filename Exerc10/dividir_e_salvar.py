def dividir_e_salvar():
    """
    Solicita ao usuário dois números (N1 e N2) 10 vezes, realiza a divisão de N1 por N2,
    e salva os resultados em um arquivo chamado 'divisao.txt'.
    Trata exceções como divisões por zero e entradas inválidas.
    """
    resultados = []

    print("Digite dois números 10 vezes (N1 e N2):")
    for i in range(1, 11):
        try:
            # Solicitando os números do usuário
            n1 = float(input(f"({i}/10) Digite o primeiro número (N1): "))
            n2 = float(input(f"({i}/10) Digite o segundo número (N2): "))

            # Realizando a divisão
            resultado = n1 / n2
            resultados.append(f"{n1} ÷ {n2} = {resultado:.2f}")
        
        except ZeroDivisionError:
            print("Erro: Não é possível dividir por zero. Resultado será ignorado.")
            resultados.append(f"{n1} ÷ {n2} = Erro (divisão por zero)")
        
        except ValueError:
            print("Erro: Entrada inválida. Apenas números são aceitos. Resultado será ignorado.")
            resultados.append("Entrada inválida")

        except Exception as e:
            print(f"Erro inesperado: {e}")
            resultados.append("Erro inesperado")

    # Salvando os resultados no arquivo
    try:
        with open("divisao.txt", "w") as arquivo:
            for linha in resultados:
                arquivo.write(linha + "\n")
        print("\nOs resultados foram salvos no arquivo 'divisao.txt'.")
    
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Chamada da função principal
if __name__ == "__main__":
    dividir_e_salvar()
