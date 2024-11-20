def exibir_palavras_terminadas_em_a(nome_arquivo):

    try:

        with open(nome_arquivo, "r") as arquivo:
            palavras = [linha.strip() for linha in arquivo.readlines()]

        palavras_terminadas_em_a = [palavra for palavra in palavras if palavra.endswith("a")]

        print("Palavras terminadas em 'a': ")
        for palavra in palavras_terminadas_em_a:
            print(palavra)


    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado")

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    nome_arquivo = "palavras.txt"
    exibir_palavras_terminadas_em_a(nome_arquivo)