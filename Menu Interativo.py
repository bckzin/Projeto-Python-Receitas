import ADD, VISU, ATUA, DEL, ALEA

file = open("BancoDados.txt","a")
cadastros = {}


while True:
    print("""
    ---------------------------------
    Gerenciamento de Receitas
    ---------------------------------

    OPÇÕES:
    [1] - ADICIONAR
    [2] - VISUALIZAR
    [3] - ATUALIZAR
    [4] - DELETAR
    [5] - SALVAR
    [6] - SAIR
    [7] - RECEITA ALEATÓRIA

    """)
    while True:
        escolha = int(input("Opção desejada : "))
        if 1 <= escolha <= 7:
            break

    if escolha == 1:  #Opção para adicionar uma receita
        cadastros = ADD.adicionar(cadastros)

    elif escolha == 2:  #Opção para visualizar receitas
        VISU.visualizar(cadastros)

    elif escolha == 3:  #Opção para atualizar uma receita
        cadastros = ATUA.atualizar(cadastros)

    elif escolha == 4:  #Opção para deletar uma receita
        cadastros = DEL.deletar(cadastros)

    elif escolha == 5:  #Opção para salvar a(s) receitas
        file=open("BancoDados.txt","a")
        file.write(str(f"{cadastros}\n"))
        print("Receitas salvas!")

    elif escolha == 6:  #Opção sair do programa
        file.close()
        exit()

    elif escolha == 7: #Opção para receita aleatória
        ALEA.aleatoria(cadastros)
    else:
        print("Opção não cadastrada.")