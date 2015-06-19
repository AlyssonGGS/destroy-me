__author__ = 'AlyssonGeraldo'
from dynamicGameObject import *
from PPlay.sprite import *
class Player(DynamicGameObject):
    def __init__(self):
        DynamicGameObject.__init__(self)
        #cria��o das coordenas e da imagem
        self.image = Sprite("player.png",1)
        self.x = 100
        self.y = 300
        self.width = self.image.width
        self.height = self.image.height
        self.image.set_position(self.x,self.y)
        #variaveis de uso da classe de fisica -> physicManager
        self.velocity = 70
        self.jumpForce = 0
        self.gravity = 50
        self.move = 0
        self.shotDirectionX = 1
        self.shotDirectionY = 0
        self.shotForce = 0
        #variaveis de controle interno da classe
        self.canJump = True
        self.canShot = False
        return

    def update(self,keyboard,deltaT):
        self.input(keyboard,deltaT)
        return

    def draw(self):
        self.image.set_position(self.x,self.y)
        self.image.draw()
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
            self.shotForce += dt * 1000
            self.canShot = False
            return
        elif self.shotForce > 0:
            self.canShot = True

        if(kb.key_pressed("SPACE") and self.canJump):
            self.jump()
            self.canJump = False
        return

    def jump(self):
        self.y -= self.height * 0.1
        self.jumpForce = 400
        return
