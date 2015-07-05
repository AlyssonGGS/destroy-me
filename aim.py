__author__ = 'AlyssonGeraldo'
from PPlay.gameimage import *
class Aim():
    def __init__(self):
        self.image = GameImage("aim.png")
        self.x = 0
        self.y = 0
        return

    def update(self, player):
        self.x = (player.x + player.width / 2) + (player.width * 1.2) * player.shotDirectionX - self.image.width/2
        self.y = player.y - (player.width ** 2 - (player.width * player.shotDirectionX) ** 2)**0.5 + self.image.height/2
        return

    def draw(self):
        self.image.set_position(self.x,self.y)
        self.image.draw()
        return