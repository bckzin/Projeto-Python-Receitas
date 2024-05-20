def visualizar(cadastros):
    try:
        with open("BancoDados.txt", "r") as file:
            pais = input("Digite o país a ser filtrado: ").capitalize()
            for linha in file:
                if pais in linha:
                    print(linha)
                else:
                    print("O país não foi encontrado")
    except FileNotFoundError:
        print("Arquivo não encontrado")
    return cadastros