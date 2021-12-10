import os
import csv


def loaddic(monsterdic):

    for filename in os.listdir():
        if filename.endswith(".mon"):
            with open(filename) as file:
                reader = csv.reader(file)
                lines = list(reader)
                monsterdic["{}".format(lines[0][0])] = lines[0][4]
            continue
    return monsterdic

def loadmonster(selectmonster,monstro):

    with open(str(selectmonster) + ".mon") as file:
        reader = csv.reader(file)
        lines = list(reader)
        monstro.nome = lines[0][0]
        monstro.hp = int(lines[0][1])
        monstro.atk = int(lines[0][2])
        monstro.code = lines[0][3]
        monstro.atributo = float(lines[0][4])
        monstro.maxhp = monstro.hp

        return monstro