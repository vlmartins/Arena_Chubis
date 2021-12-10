import random


class Player:

    def __init__(self, hp, atk, nome, raca):
        self.hp = hp
        self.atk = atk
        self.nome = nome
        self.maxhp = self.hp
        self.raca = raca
        self.token = 0
        self.espada = 0

    def dano(self):
        return random.randint(1, self.atk)

    def vida(self):
        if self.raca == "Elfo":
            return random.randint(2, self.atk * 3)
        else:
            return random.randint(1, self.atk)

    def playerlvl(self):
        if self.raca == "Elfo":
            self.hp = self.maxhp
            atkf = self.atk * 5 * 3
            total = atkf + self.hp
            playerlvl = total / 6
            return playerlvl
        self.hp = self.maxhp
        atkf = self.atk * 5
        total = atkf + self.hp
        playerlvl = total / 6
        return playerlvl

    def setmaxhp(self):
        self.hp = self.maxhp




