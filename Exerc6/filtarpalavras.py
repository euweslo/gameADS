def filtrar_palavras(nome_arquivo_entrada, nome_arquivo_saida):
    """
    Lê palavras de um arquivo e salva em outro arquivo as palavras
    que começam com 'B' e terminam com 'O'.
    """
    try:
        # Lendo as palavras do arquivo de entrada
        with open(nome_arquivo_entrada, "r") as arquivo_entrada:
            palavras = [linha.strip() for linha in arquivo_entrada.readlines()]
        
        # Filtrando palavras que começam com 'B' e terminam com 'O'
        palavras_filtradas = [palavra for palavra in palavras if palavra.startswith("B") and palavra.endswith("o")]
        
        # Salvando as palavras filtradas no arquivo de saída
        with open(nome_arquivo_saida, "w") as arquivo_saida:
            for palavra in palavras_filtradas:
                arquivo_saida.write(palavra + "\n")
        
        print(f"As palavras filtradas foram salvas em '{nome_arquivo_saida}'.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo_entrada}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Chamada da função
if __name__ == "__main__":
    nome_arquivo_entrada = "Palavras.txt"
    nome_arquivo_saida = "PalavrasFiltradas.txt"
    filtrar_palavras(nome_arquivo_entrada, nome_arquivo_saida)
