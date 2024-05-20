def comentario(cadastros):
    with open("BancoDados.txt", "r") as arquivo:
        for linha in arquivo:
            if "COMENTÁRIOS :" in linha:
                comentario = linha.split("COMENTÁRIOS :")[1].strip()
                if comentario:
                    print(linha)
    return cadastros