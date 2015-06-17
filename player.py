__author__ = 'AlyssonGeraldo'
from dynamicGameObject import *
from PPlay.sprite import *
class Player(DynamicGameObject):
    def __init__(self):
        DynamicGameObject.__init__(self)
        #criação das coordenas e da imagem
        self.image = Sprite("player.png",1)
        self.x = 100
        self.y = 300
        self.width = self.image.width
        self.height = self.image.height
        self.image.set_position(self.x,self.y)
        #variaveis de uso da classe de fisica -> physicManager
        self.jumpForce = 0
        self.gravity = 50
        self.move = 0
        #variaveis de controle interno da classe
        self.canJump = True
        return

    def update(self,keyboard):
        self.input(keyboard)
        return

    def draw(self):
        self.image.set_position(self.x,self.y)
        self.image.draw()
        return

    def input(self,kb):
        if(kb.key_pressed("RIGHT")):
            self.move = 1
        elif(kb.key_pressed("LEFT")):
            self.move = -1
        else:
            self.move = 0
        if(kb.key_pressed("SPACE") and self.canJump):
            self.jump()
            self.canJump = False
        return

    def jump(self):
        self.y -= self.height * 0.1
        self.jumpForce = 400
        return
