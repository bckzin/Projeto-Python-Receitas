import random

def aleatoria(cadastros):
    burrata_gratinada = {"nome": "Burrata gratinada", "origem": "Itália", "ingredientes": "1 brunata, 1 xícara de chá de tomates cereja, azeite de oliva, sal e manjeiricão", "preparo": "refogue os tomates no azeite, tempere, coloque a burrata, misture, leve ao forno a 220ºC por 20 min"}
    creme_brulee = {"nome": "Creme Bruleé", "origem": "França", "ingredientes": "500ml de creme de leite, 6 gemas e 100 g de açúcar", "preparo": "Pré-aqueça o forno a 180ªC, aqueça o creme na panela, misture numa tigela as gemas e o açúcar. Junte o creme de leite mexendo bem e leve ao forno por 30 min"}
    sorteio = [burrata_gratinada, creme_brulee]
    sorteio = random.choice(sorteio)
    print(sorteio)
    return cadastros