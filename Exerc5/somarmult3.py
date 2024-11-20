def somar_multiplos_de_tres(nome_arquivo):
    """
    Lê um arquivo e soma apenas os valores múltiplos de 3.
    """
    try:
        # Abrindo o arquivo para leitura
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        
        # Convertendo as linhas para números inteiros
        numeros = [int(linha.strip()) for linha in linhas]
        
        # Filtrando e somando apenas os múltiplos de 3
        soma = sum(numero for numero in numeros if numero % 3 == 0)
        print(f"A soma dos números múltiplos de 3 é: {soma}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except ValueError:
        print("Erro: O arquivo contém valores que não são números inteiros.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Chamada da função
if __name__ == "__main__":
    nome_arquivo = "lista.txt"
    somar_multiplos_de_tres(nome_arquivo)
