from divisao_pacote.divisao import dividir

def main():
    nome_arquivo = "valores.txt"
    
    try:
        # Lendo os valores do arquivo
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
        
        print("Resultados das divisões:")
        for linha in linhas:
            try:
                valor = int(linha.strip())  # Convertendo cada linha para inteiro
                resultado = dividir(valor, 2)  # Dividindo o valor por 2
                if resultado is not None:  # Exibe o resultado apenas se não houver erro
                    print(f"{valor} ÷ 2 = {resultado}")
            except ValueError:
                print(f"Erro: A linha '{linha.strip()}' não é um número válido.")
    
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()



