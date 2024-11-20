def mostrar_palavras_m_a(nome_arquivo):
    """
    Lê um arquivo e exibe palavras que começam com 'M' ou 'm'
    e terminam com 'A' ou 'a'.
    """
    try:
        # Abrindo o arquivo para leitura
        with open(nome_arquivo, "r") as arquivo:
            palavras = [linha.strip() for linha in arquivo.readlines()]

        # Filtrando palavras que começam com 'M' e terminam com 'A'
        palavras_filtradas = [
            palavra for palavra in palavras if palavra.lower().startswith("m") and palavra.lower().endswith("a")
        ]

        # Exibindo as palavras encontradas
        print("Palavras que começam com 'M' e terminam com 'A':")
        if palavras_filtradas:
            for palavra in palavras_filtradas:
                print(palavra)
        else:
            print("Nenhuma palavra encontrada com esses critérios.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Chamada da função principal
if __name__ == "__main__":
    nome_arquivo = "palavras3.txt"
    mostrar_palavras_m_a(nome_arquivo)
