__author__ = 'AlyssonGeraldo'
from PPlay.gameimage import *
class PlayerUI():
    def __init__(self,maxLife,playersNum,janela):
        self.wind = janela
        self.lifes = self.createMatrix(playersNum,maxLife)
        for i in range(playersNum):
            for life in range(maxLife):
                self.lifes[i][life].set_position(50 * (life + 1), 50 * (i + 1))
        return

    def update(self,players):
        return

    def draw(self,players):
        for i in range(len(players)):
            self.wind.draw_text("Player " + str(i + 1), 200, (50 * (i + 1))  , size=40, color=(0,0,0), font_name="Arial", bold=False, italic=False)
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