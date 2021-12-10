import csv
import Player as p

def load_game(jogador):
    try:
        with open(str(jogador.nome) + ".ply") as file:
            reader = csv.reader(file)
            lines = list(reader)
            jogador.nome = lines[0][0]
            jogador.atk = int(lines[0][1])
            jogador.raca = lines[0][2]
            jogador.maxhp = int(lines[0][3])
            jogador.hp = jogador.maxhp
            return jogador
    except:
        None


def frist_save(jogador):
    #Cria um arquivo do jogador sendo cada coluna respectivamente:
    #Nome, ataque, raça, vida, kills, k/d
    try:
        with open(str(jogador.nome) +".ply", "w+", newline='') as file:
            file.write("{},{},{},{}, , ".format(jogador.nome, jogador.atk, jogador.raca, jogador.maxhp))
            print("Jogador salvo com sucesso!")
        return
    except: print("Falha ao salvar!!!")

def combat_save(jogador, monstro, game_state):
    try:
        with open(str(jogador.nome)+".ply", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            lines[0][5] += str(game_state)
            lines[0][3] = jogador.maxhp
            lines[0][1] = jogador.atk

            if game_state == 1:
                lines[0][4] += monstro.code

        with open(str(jogador.nome)+".ply", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        return print("Jogador salvo com sucesso!")
    except: print("Falha ao salvar!!!")

def item_save(jogador):
    try:
        with open(str(jogador.nome)+".ply", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            lines[0][3] = jogador.maxhp
            lines[0][1] = jogador.atk


        with open(str(jogador.nome)+".ply", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(lines)
        return print("Jogador salvo com sucesso!")
    except: print("Falha ao salvar!!!")