def chk_name(jogador):
    try:
        with open(str(jogador.nome)+".ply", "r") as file:
            print("Jogador " + jogador.nome + " já existe!")
            return False
    except: None

def is_monstro(nome):
    try:
        with open(nome+".mon", "r") as file:
            print("Monstro " + nome + " já existe!")
            return False
    except: None