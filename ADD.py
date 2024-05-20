def adicionar(cadastros):
    while True:
        receita = input("Nome da receita : ")
        pais = input("País de Origem : ").capitalize()
        qntd = int(input("\nQuantidade de ingredientes : "))
        print("-Lista de Ingredientes-")
        lista_ing = []
        for i in range(qntd):
            ingredientes = (input(f"{i + 1}º Ingrediente : "))
            lista_ing.append(f"{i + 1}º ingrediente = {ingredientes}")
        ing = ", ".join(lista_ing)

        passos = int(input("\nQuantidade de passos do preparo : "))
        print("-Passos do Preparo-")
        lista_prep = []
        for j in range(passos):
            preparo = (input(f"{j + 1}º Passo : "))
            lista_prep.append(f"{j + 1}º passo = {preparo}")
        prep = ", ".join(lista_prep)

        adicionar_comentario = input("Deseja adicionar comentários sobre a receita? [S] ou [N] : ").upper()
        comentarios = ""
        if adicionar_comentario == "S":
            comentarios = input("Comentários sobre a receita : ")
        
        favoritar = input("Deseja adicionar essa receita aos favoritos [S] ou [N] : ").upper()
        if favoritar == "S":
            arquivo = open("favoritos.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep} | COMENTÁRIOS : {comentarios}\n")

            arquivo = open("BancoDados.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep} | COMENTÁRIOS : {comentarios}\n")
        elif favoritar == "N":
            arquivo = open("BancoDados.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep} | COMENTÁRIOS : {comentarios}\n")
            
        continuar = input("Deseja continuar adicionando receitas [S] ou [N] : ").upper()
        if continuar == "N":
            arquivo.close()
            break
        elif continuar != "S":
            print("Opção inválida, saindo...")
            break 
    return cadastros