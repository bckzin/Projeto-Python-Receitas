def visualizar(cadastros):
    file = open("BancoDados.txt", "r")
    pais = input("Digite o país a ser filtrado: ").capitalize()
    for linha in file:
        if pais in linha:
            print(linha)
    return cadastros