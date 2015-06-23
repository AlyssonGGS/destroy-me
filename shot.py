__author__ = 'AlyssonGeraldo'
from dynamicGameObject import *
from PPlay.gameimage import *

class Shot(DynamicGameObject):
    def _init_(self):
        print("Ola")
        self.image = GameImage("cannonball.png")
        self.direction = (0,0)
        self.forceX = 0
        self.forceY = 0
        self.gravity = 50
        self.destroy = False
        return

    def draw(self):
        self.image.set_position(self.x,self.y)
        self.image.draw()
        return