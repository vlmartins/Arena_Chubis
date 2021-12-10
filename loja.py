import csv
import loader as l
jogador = ""


def loja(jogador):
    Notokens = "Você não tem tokens para comprar esse item!"
    itensdic = {}
    print(f"Você tem {jogador.token} token(s) para gastar")
    with open("itens.inv") as file:
        reader = csv.reader(file)
        itenslist = list(reader)

    for itens in itenslist:
        itensdic["{}".format(itens[0])] = int(itens[1])

    lista = 1
    for key, value in itensdic.items():
        print(f"({lista}) {key} por {value} tokens.")
        lista += 1
    print("(4) SAIR")
    escolhas = opcoes4()
    if escolhas == 1:
        if jogador.token - 3 >= 0:
            jogador.token -= 3
            jogador.maxhp += 1
            input("A runa faz efeito e você se sente mais vigoroso! (...)")
        else:
            input(Notokens)

    if escolhas == 2:
        if jogador.token - 10 >= 0:
            jogador.token -= 10
            jogador.atk += 1
            input("A runa faz efeito e você se sente mais poderoso! (...)")
        else:
            input(Notokens)

    if escolhas == 3:
        if jogador.token - 200 >= 0:
            jogador.token -= 200
            jogador.espada = 1
            input("Você equipa a espada e não parece surtir efeito nenhum!")
        else:
            input(Notokens)
    if escolhas == 4:
        pass
    l.item_save(jogador)
    return jogador

def opcoes4():
    escolha = input()
    if escolha == "1":
        return 1
    elif escolha == "2":
        return 2
    elif escolha == "3":
        return 3
    elif escolha == "4":
        return 4
    else:
        print("Opção inválida")
        return opcoes4()



