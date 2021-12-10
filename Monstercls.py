import random

class Monstro:

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
