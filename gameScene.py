__author__ = 'AlyssonNote'
from scene import *
from physicManager import *
from mapManager import *
from player import *

#cena do jogo principal
class GameScene(Scene):
    def __init__(self):
        #instancia dos grupos de controle do gerenciador de fisica
        self.gravityObjects = []
        self.players = []
        #objeto que vai gerenciar os blocos. Possivelmente ficará com a maior parte da colisao
        self.mapMan = MapManager()
        #criar os players
        self.player = Player()
        #adiciona as variaveis aos grupos de controle usados pelo gerenciador de fisica
        self.gravityObjects.append(self.player)
        self.players.append(self.player)
        #gerenciador de fisica do jogo
        self.physManager = PhysicManager()
        return

    def update(self,deltaT,keyboard):
        self.player.update(keyboard)
        #parte dedicada a atualização da fisica
        self.physManager.collisionPlayerVSBricks(self.player,self.mapMan.bricks)
        self.physManager.gravity(deltaT,self.gravityObjects)#aplica a gravidade
        self.physManager.playerMove(deltaT,self.player)#movimento do player
        self.physManager.applyJump(deltaT,self.player)
        #--------------------------------------
        return

    #desenha todos os blocos
    def draw(self):
        self.mapMan.draw()
        self.player.draw()
        return

    #usado para alguns testes
    #não entrará no jogo
    def mostrar(self,cels):
        for c in cels:
            print((c))
        return