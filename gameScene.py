__author__ = 'AlyssonNote'
from scene import *
from physicManager import *
from mapManager import *
from player import *
from turnManager import *
from aim import *
from shot import *

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
        #mira desenhada na tela
        self.aim = Aim()
        #adiciona as variaveis aos grupos de controle usados pelo gerenciador de fisica
        self.gravityObjects.append(self.player)
        self.gravityObjects.append(self.player2)
        self.players.append(self.player)
        self.players.append(self.player2)
        #gerenciador de fisica do jogo
        self.physManager = PhysicManager()
        self.turnManager = TurnManager(self.players)
        #tiro
        self.shot = None
        return

    def update(self,deltaT,keyboard):
        self.turnManager.actualPlayer.update(keyboard,deltaT)
        #parte dedicada a atualização da fisica
        for player in self.turnManager.players:
            self.physManager.collisionPlayerVSBricks(player,self.mapMan.bricks)#colisao entre players e blocos
        self.physManager.gravity(deltaT, self.gravityObjects)#aplica a gravidade
        if self.turnManager.actualPlayer.jumpForce != 0:
            self.physManager.applyJump(deltaT, self.turnManager.actualPlayer)#faz o calculo do pulo do player atual
        self.physManager.playerMove(deltaT, self.turnManager.actualPlayer)#movimento do player
        if self.turnManager.actualPlayer.canShot == True:#caso o player possa atirar
            self.turnManager.actualPlayer.canShot = False
            self.createShot()
        if self.shot != None:
            self.physManager.shotMove(self.shot,deltaT)
            if self.physManager.collisionPlayerVSBall(self.turnManager.othersPlayers,self.shot):
                self.turnManager.changePlayer()
                self.shot = None
        #--------------------------------------
        self.aim.update(self.turnManager.actualPlayer)#a mira segue o jogador
        return

    #desenha todos os blocos
    def draw(self):
        self.mapMan.draw()
        for player in self.turnManager.players:
            player.draw()
        self.aim.draw()
        if self.shot != None:
            self.shot.draw()
        return

    def createShot(self):
        self.shot = Shot()
        self.shot._init_()
        self.shot.x = self.aim.x
        self.shot.y = self.aim.y
        self.shot.force = self.turnManager.actualPlayer.shotForce
        self.turnManager.actualPlayer.shotForce = 0
        self.shot.direction = (self.turnManager.actualPlayer.shotDirectionX,self.turnManager.actualPlayer.shotDirectionY)
        self.gravityObjects.append(self.shot)
        return