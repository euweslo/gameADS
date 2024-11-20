def salvar_palavras():
    """
    Solicita 10 palavras ao usuário e as salva em dois arquivos:
    - palavras_a.txt: palavras que começam com 'a' ou 'A'.
    - demais_palavras.txt: palavras que não começam com 'a' ou 'A'.
    """
    palavras_a = []
    demais_palavras = []

    print("Digite 10 palavras:")
    for _ in range(10):
        palavra = input("Digite uma palavra: ").strip()
        if palavra.lower().startswith('a'):
            palavras_a.append(palavra)
        else:
            demais_palavras.append(palavra)

    # Salvando as palavras em arquivos
    try:
        with open("palavras_a.txt", "w") as arquivo_a:
            for palavra in palavras_a:
                arquivo_a.write(palavra + "\n")
        
        with open("demais_palavras.txt", "w") as arquivo_d:
            for palavra in demais_palavras:
                arquivo_d.write(palavra + "\n")
        
        print("As palavras foram salvas nos arquivos:")
        print("- palavras_a.txt: palavras que começam com 'a'")
        print("- demais_palavras.txt: demais palavras")

    except Exception as e:
        print(f"Erro ao salvar os arquivos: {e}")

# Chamada da função principal
if __name__ == "__main__":
    salvar_palavras()
