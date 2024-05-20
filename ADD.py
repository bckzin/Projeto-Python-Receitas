def adicionar(cadastros):
    while True:
        receita = input("\nNome da receita : ")
        pais = input("País de Origem : ").capitalize()

        ingredientes = []
        preparo = []

        qntd = int(input("Quantidade de ingredientes : "))
        print("\n-Lista de Ingredientes-")
        for i in range(qntd):
            ingredientes.append(input(f"{i + 1}º Ingrediente : "))

        passos = int(input("Quantidade de passos do preparo : "))
        print("\n-Passos do Preparo-")
        for j in range(passos):
            preparo.append(input(f"{j+ 1}º Passo : "))

        cadastros[receita] = {"origem": pais, "ingredientes": ingredientes, "preparo": preparo}

        continuar = ""
        while continuar != "S":
            continuar = input("Deseja continuar adicionando receitas [S] ou [N] : ").upper()

            if continuar == "N":
                print(cadastros)
                return cadastros

            elif continuar != "S":
                print("Opção inválida!")