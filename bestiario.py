import random
import chk_name
import re



class Monstro():

    # construtor
    def __init__(self, nome, hp, atk, code, atributo):
        self.hp = hp
        self.atk = atk
        self.code = code
        self.mlevel = (self.hp + (self.atk * 5)) / 6
        self.nome = nome
        self.atributo = atributo
        self.maxhp = self.hp


    def dano(self):
        return random.randint(1, self.atk)

    def get_codigo(self):
        return self.code

    def get_monster_level(self):
        return ((int(self.hp) + (int(self.atk) * 5)) / 6)

def gerador_de_monstro():
    # Gera arquivo .mon com os dados do monstro

    invalid_name_msg = "Nome Inválido. Aceita apenas nome com letras."
    invalid_int_msg = "Só aceita números!"
    name_regex = "^([a-zA-Z]+\s?[a-zA-Z]+)+?$"
    int_regex = "^[1-9][0-9]*$"
    code_regex = "^[a-zA-Z0-9]$"

    nome = input("Qual nome do seu monstro? ")
    is_valid_name = bool(re.search(name_regex, nome))

    while (is_valid_name and chk_name.is_monstro(nome)) is False:
        print(invalid_name_msg)
        nome = input("Insira o nome do seu monstro novamente: ")
        is_valid_name = bool(re.search(name_regex, nome))

    hp = input("Quantos pontos de vida tem seu monstro?")
    int_validator = bool(re.search(int_regex, hp))

    while int_validator is False:
        print(invalid_int_msg)
        hp = input("Quantos pontos de vida tem seu monstro? ")
        int_validator = bool(re.search(int_regex, hp))

    atk = input("Quanto tem de ataque seu monstro? ")
    int_validator = bool(re.search(int_regex, atk))

    while int_validator is False:
        print(invalid_int_msg)
        atk = input("Quanto tem de ataque seu monstro? ")
        int_validator = bool(re.search(int_regex, atk))

    code = input("Qual código do seu monstro? Só pode uma letra ou um número: ")
    code_validator = bool(re.search(code_regex, code))

    while code_validator is False:
        print("Código errado!")
        code = input("Qual código do seu monstro? Só pode uma letra ou um número? ")
        code_validator = bool(re.search(code_regex, code))

    nivel = ((int(hp) + (int(atk) * 5)) / 6)

    try:
        with open(nome + ".mon", "w+") as file:
            file.write("{},{},{},{},{},Monster ".format(nome, hp, atk, code, nivel))
            print("Monstro salvo com sucesso!")
            print(
                "Você gerou um {} com {} pontos de vida e {} de ataque. O código do monstro é {}.".format(nome, hp, atk,
                                                                                                          code))
        pass
    except:
        print("Falha ao salvar!!!")

gerador_de_monstro()