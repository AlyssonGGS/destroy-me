__author__ = 'AlyssonNote'
from PPlay.gameimage import *
from PPlay.gameobject import *

#objeto que formará o cenario
class Brick(GameObject):

    def __init__(self,x = 0, y = 0):
        GameObject.__init__(self)
        #instancia a imagem
        self.image = GameImage("brick.png")
        #define as posicoes x,y
        self.x = x
        self.y =  y
        self.width = self.image.width
        self.height = self.image.height
        self.image.set_position(x,y)
        return

    def draw(self):
        self.image.draw()
        return