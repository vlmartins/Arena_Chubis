# Arena Chubis
versao = "V.01"
game_state = 0
import re
import random
import Player as p
import loader as l
import chk_name
import mloader as m
import loja
import Monstercls as mcls

def main():
    '''menu do jogo'''
    print("Bem vindo a Arena dos monstros versão " + versao)
    input("Para continuar aperte qualquer tecla (Cont.)")
    print("Você quer começar um jogo(1) ou carregar(2)")
    escolhas = opcoes2()
    if escolhas == 1:
        jogador = criarJogador()
        monstro = mcls.Monstro("Goblin", 10, 2, "g", 5)
        combate1(jogador, monstro)

    elif escolhas == 2:
        jogador = p.Player(0, 0, "", "")
        jogador.nome = input("Insira o nome do jogador gravado: ")
        l.load_game(jogador)
        if l.load_game(jogador) is None:
            print("Jogador inválido! Comece outra vez.")
            main()
        else:
            print("Bem vindo " + jogador.nome + ", nobre " + jogador.raca)
            city(jogador)


def criarJogador():
    invalid_name_msg = "Nome Inválido. Aceita apenas nome com letras."
    jogador = p.Player(0, 0, "", "")
    nome = input("Insira seu Nome e Sobrenome:")
    name_validator = bool(re.search("^([a-zA-Z]+\s?[a-zA-Z]+)+?$", nome))
    jogador.nome = str(nome)

    while (name_validator and chk_name.chk_name(jogador)) is False:
        print(invalid_name_msg)
        nome = input("Insira seu Nome e Sobrenome novamente:")
        name_validator = bool(re.search("^([a-zA-Z]+\s?[a-zA-Z]+)+?$", nome))
        jogador.nome = str(nome)

    jogador.nome = str(nome)
    print("Bem vindo " + nome + ".")
    print(str(jogador.nome) + " você é Humano(1), Elfo(2), Anao(3)?")
    escolher3opcoes = opcoes3()

    if escolher3opcoes == 1:
        jogador.raca = "Humano"
        jogador.hp = 10
        jogador.atk = 4
        jogador.maxhp = jogador.hp
    elif escolher3opcoes == 2:
        jogador.raca = "Elfo"
        jogador.hp = 5
        jogador.atk = 2
        jogador.maxhp = jogador.hp
    elif escolher3opcoes == 3:
        jogador.raca = "Anao"
        jogador.hp = 15
        jogador.atk = 3
        jogador.maxhp = jogador.hp
    l.frist_save(jogador)
    return jogador


def monsterlib(monsterdic):
    m.loaddic(monsterdic)
    return monsterdic


def progresso(jogador, monstro):
    playerlvl = jogador.playerlvl()
    monsterdic = {}
    monsterlib(monsterdic)
    monsterlist = []

    for monster, level in monsterdic.items():
            if float(level) < float(playerlvl * 1.3) and float(level) > float(playerlvl * 0.8):
                monsterlist.append(monster)

    monster_count = len(monsterlist)

    if monster_count > 0:
        selectmonster = monsterlist[random.randint(0, int(len(monsterlist)) - 1)]
        m.loadmonster(selectmonster, monstro)

    else:
        print("Não encontramos nenhum monstro a sua altura ou digno de uma batalha... Você está na ARENA, você já saiu para o BESTIARIO?")
        city(jogador)

    return monstro


def city(jogador):
    print("Você quer ir para a LOJA(1) ou ARENA(2) ou SAIR(3)")
    escolhas = opcoes3()
    if escolhas == 2:
        monstro = mcls.Monstro("",1,1,"","")
        progresso(jogador,monstro)
        combate1(jogador, monstro)
    elif escolhas == 1:
        loja.loja(jogador)
        city(jogador)
    elif escolhas == 3:
        quit()

def opcoes2():
    escolha = input()
    if escolha == "1":
        return 1
    elif escolha == "2":
        return 2
    else:
        print("Opção inválida")
        return opcoes2()


def opcoes3():
    escolha = input()
    if escolha == "1":
        return 1
    elif escolha == "2":
        return 2
    elif escolha == "3":
        return 3
    else:
        print("Opção inválida")
        return opcoes3()




def chk_vitoria(jogador_hp, monstro_hp):
    global game_state

    if monstro_hp < 1:
        input("Ganhasse, éx um monxtro, não pera... (Cont.)")
        game_state = 1

    elif jogador_hp < 1:
        input("Laranja, perdesse. (Cont.)")
        game_state = 2
    else:
        game_state = 0


def combate1(jogador, monstro):
    print("Seu duelo será contra " + monstro.nome)
    print("Prepare-se " + str(jogador.nome) + ", o inimigo se apróxima! ATACAR(1) ou se CURAR(2)")
    jogador.hp = jogador.maxhp
    chk_vitoria(jogador.hp, monstro.hp)

    tokens_vitoria = float(monstro.atributo // 2.2)



    while game_state == 0:
        print("Sua vida:" + str(jogador.hp) + "." + " Inimigo:" + str(monstro.hp))
        escolha = input()

        if escolha == "1":
            monstro.hp -= jogador.dano()

            chk_vitoria(jogador.hp, monstro.hp)
            if game_state == 1:
                break

            print("Ele revida!")
            jogador.hp -= monstro.dano()

            chk_vitoria(jogador.hp, monstro.hp)
            if game_state == 2:
                break

        elif escolha == "2":
            jogador.hp += jogador.vida()
            print("Você se cura!")

            print("Ele revida!")
            jogador.hp -= monstro.dano()

            chk_vitoria(jogador.hp, monstro.hp)
            if game_state == 2:
                break
        else:
            print("Comando Inválido")
    l.combat_save(jogador, monstro, game_state)
    if game_state == 1:
        jogador.token += tokens_vitoria
        input(f"Você ganhou {tokens_vitoria} token(s) (...) ")


    city(jogador)

main()