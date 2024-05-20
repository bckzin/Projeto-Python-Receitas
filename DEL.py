def deletar(cadastros):
    nome_receita = input("Nome da receita que você quer deletar: ")

    with open("BancoDados.txt", "r") as file:
        linhas = file.readlines()

    with open("BancoDados.txt", "w") as file:
        for linha in linhas:
            if nome_receita not in linha:
                file.write(linha)
            else:
                print("Receita deletada")
    if nome_receita in cadastros:
        del cadastros[nome_receita]
    
    return cadastros