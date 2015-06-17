__author__ = 'AlyssonNote'
from scene import *
from physicManager import *
from mapManager import *
from player import *
from turnManager import *

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
        self.player2 = Player()
        #adiciona as variaveis aos grupos de controle usados pelo gerenciador de fisica
        self.gravityObjects.append(self.player)
        self.gravityObjects.append(self.player2)
        self.players.append(self.player)
        self.players.append(self.player2)
        #gerenciador de fisica do jogo
        self.physManager = PhysicManager()
        self.turnManager = TurnManager(self.players)
        return

    def update(self,deltaT,keyboard):
        self.turnManager.actualPlayer.update(keyboard)
        #parte dedicada a atualização da fisica
        for player in self.turnManager.players:
            self.physManager.collisionPlayerVSBricks(player,self.mapMan.bricks)
        self.physManager.gravity(deltaT,self.gravityObjects)#aplica a gravidade
        self.physManager.playerMove(deltaT,self.turnManager.actualPlayer)#movimento do player
        self.physManager.applyJump(deltaT,self.turnManager.actualPlayer)
        #--------------------------------------
        return

    #desenha todos os blocos
    def draw(self):
        self.mapMan.draw()
        for player in self.turnManager.players:
            player.draw()
        return

    #usado para alguns testes
    #não entrará no jogo
    def mostrar(self,cels):
        for c in cels:
            print((c))
        return