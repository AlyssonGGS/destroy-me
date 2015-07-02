__author__ = 'AlyssonGeraldo'
from PPlay.window import *
from player import *
from mapManager import *

class World():
    def __init__(self,janela,maxLife):
        self.x = 0
        self.y = 0
        self.players = []
        self.createPlayer(200,200,maxLife)
        self.createPlayer(100,100,maxLife)
        self.mapMan = MapManager()
        return

    def createPlayer(self,x,y,mLife):
        player = Player(x,y,mLife)
        self.players.append(player)
        return

    def draw(self,turnMan):
        self.mapMan.draw()
        for player in turnMan.players:
            player.draw()
        return
