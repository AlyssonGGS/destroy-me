__author__ = 'AlyssonGeraldo'
from PPlay.gameimage import *
class PlayerUI():
    def __init__(self,maxLife,playersNum):
        self.lifes = self.createMatrix(playersNum,maxLife)
        for i in range(playersNum):
            for life in range(maxLife):
                self.lifes[i][life].set_position(50 * (life + 1), 50 * (i + 1))
        return

    def update(self,players):
        return

    def draw(self,players):
        for i in range(len(players)):
            for j in range(players[i].life):
                self.lifes[i][j].draw()
        return

    def createMatrix(self,r,c):
        matriz = []
        for i in range(r):
            lifes = []
            for j in range(c):
                lifes.append(GameImage("life.png"))
            matriz.append(lifes)
        return matriz