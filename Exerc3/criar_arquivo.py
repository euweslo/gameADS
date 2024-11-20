def criar_arquivo(nome_arquivo, conteudo):
    """
    Cria um arquivo .txt com o nome especificado e escreve o conteúdo fornecido.
    """
    try:
        with open(f"{nome_arquivo}.txt", "w") as arquivo:
            arquivo.write(conteudo)
        print(f"Arquivo '{nome_arquivo}.txt' criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar o arquivo: {e}")


def main():
    # Solicita o nome do arquivo e o conteúdo ao usuário
    nome = input("Digite o nome do arquivo (sem extensão): ")
    conteudo = input("Digite o conteúdo para o arquivo: ")
    
    # Chama a função para criar o arquivo
    criar_arquivo(nome, conteudo)

if __name__ == "__main__":
    main()
