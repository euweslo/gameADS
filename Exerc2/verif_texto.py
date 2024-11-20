def verificar_inicio(texto):
   
    if texto.startswith("Olá"):
        print("Sim, o texto começa com 'Olá'.")
    else:
        print("Não, o texto não começa com 'Olá'.")

def main():
    frase = input("Digite uma frase: ")
    
    verificar_inicio(frase)

if __name__ == "__main__":
    main()