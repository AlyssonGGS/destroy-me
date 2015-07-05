__author__ = 'AlyssonGeraldo'
from dynamicGameObject import *
from PPlay.sprite import *
from soundManager import *
class Player(DynamicGameObject):
    def __init__(self,x,y,maxLife,side):
        DynamicGameObject.__init__(self)
        #criação das coordenas e da imagem
        self.x = x
        self.y = y
        self.image = Sprite("player.png", 1)
        self.imageI = Sprite("playerI.png", 1)
        if side == "r":
            self.actualImage = self.image
            self.shotDirectionX = 1
        else:
            self.actualImage = self.imageI
            self.shotDirectionX = -1
        self.shotDirectionY = 0
        self.width = self.image.width
        self.height = self.image.height
        self.refreshPosition()
        #vidas
        self.life = maxLife
        #variaveis de uso da classe de fisica -> physicManager
        self.velocity = 70
        self.jumpForce = 0
        self.gravity = 50
        self.move = 0
        self.shotForceX = 0
        self.shotForceY = 0
        #variaveis de controle interno da classe
        self.canJump = True
        self.shooted = False
        return

    def update(self,keyboard,deltaT):
        self.input(keyboard,deltaT)
        if self.shotDirectionX < 0:
            self.actualImage = self.imageI
        else:
            self.actualImage = self.image
        return

    def draw(self):
        self.refreshPosition()
        self.actualImage.draw()
        return

    def input(self,kb,dt):
        if(kb.key_pressed("RIGHT")):
            self.move = 1
        elif(kb.key_pressed("LEFT")):
            self.move = -1
        else:
            self.move = 0

        if(kb.key_pressed("UP")):
            self.shotDirectionX -= dt
            if self.shotDirectionX < -1:
                self.shotDirectionX = -1
            self.shotDirectionY = 1 - abs(self.shotDirectionX)
        elif(kb.key_pressed("DOWN")):
            self.shotDirectionX += dt
            if self.shotDirectionX > 1:
                self.shotDirectionX = 1
            self.shotDirectionY = 1 - abs(self.shotDirectionX)

        if kb.key_pressed("RETURN"):
            self.shotForceX += dt * 500
            self.shotForceY += dt * 500
            self.move = 0
            return
        elif self.shotForceX > 0:
            self.shooted = True

        if(kb.key_pressed("SPACE") and self.canJump):
            self.jump()

        return

    def jump(self):
        self.y -= self.height * 0.1
        self.jumpForce = 300
        self.canJump = False
        self.gravity = 80
        return

    def refreshPosition(self):
        self.image.set_position(self.x,self.y)
        self.imageI.set_position(self.x,self.y)
        self.actualImage.set_position(self.x,self.y)
        return