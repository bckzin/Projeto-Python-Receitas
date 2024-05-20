##teste##

import random

def aleatoria(cadastros):
    for chave, valor in cadastros.items():
        print(f"{chave}: {valor}")

#Exemplo de uso
burrata_gratinada = {
    "Receita": "Burrata Gratinada",
    "origem": "Itália",
    "ingredientes": "1 burrata, 1 xícara de chá de tomates cereja, azeite de oliva, sal e manjericão",
    "preparo": "Refogue os tomates no azeite, tempere, coloque a burrata, misture, leve ao forno a 220ºC por 20 minutos."
}
creme_brulee = {
    "Receita": "Creme Brulee",
    "origem": "França",
    "ingredientes": "500 ml de creme de leite, 6 gemas e 100 g de açúcar",
    "preparo": "Pré-aqueça o forno a 180ºC, aqueça o creme de leite na panela, misture numa tigela as gemas e o açúcar. Junte o creme de leite mexendo bem e leve ao forno por 30 minutos."
}
sorteio = [burrata_gratinada, creme_brulee]

#Exibindo os dicionários

print(random.choice(sorteio))

