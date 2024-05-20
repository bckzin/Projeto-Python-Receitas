def adicionar(cadastros):
    while True:
        receita = input("Nome da receita : ")
        pais = input("País de Origem : ").capitalize()
        qntd = int(input("\nQuantidade de ingredientes : "))
        print("-Lista de Ingredientes-")
        for i in range(qntd):
            lista_ing = []
            ingredientes = (input(f"{i + 1}º Ingrediente : "))
            lista_ing.append(f"{i + 1}º ingrediente = {ingredientes}")
            ing = ", ".join(lista_ing)

        passos = int(input("\nQuantidade de passos do preparo : "))
        print("-Passos do Preparo-")
        for j in range(passos):
            lista_prep = []
            preparo = (input(f"{j + 1}º Passo : "))
            lista_prep.append(f"{i + 1}º passo = {preparo}")
            prep = ", ".join(lista_prep)

        favoritar = input("Deseja adicionar essa receita aos favoritos [S] ou [N] : ").upper()
        if favoritar == "S":
            arquivo = open("favoritos.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep}\n")
        elif favoritar == "N":
            arquivo = open("BancoDados.txt", "a")
            arquivo.write(f"RECEITA : {receita} | ORIGEM : {pais} | INGREDIENTES : {ing} | PREPARO : {prep}\n")

        continuar = input("Deseja continuar adicionando receitas [S] ou [N] : ").upper()
        if continuar == "N":
            arquivo.close()
            break
        elif continuar != "S":
            print("Opção inválida, saindo...")
            break 
    return cadastros