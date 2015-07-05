__author__ = 'AlyssonNote'
from scene import *
from physicManager import *
from world import *
from turnManager import *
from aim import *
from shot import *
from PlayerUI import *

#cena do jogo principal
class GameScene(Scene):
    def __init__(self,janela):
        self.maxLife = 3
        #instancia dos grupos de controle do gerenciador de fisica
        self.gravityObjects = []
        #criar os players
        self.world = World(janela,self.maxLife)
        #mira desenhada na tela
        self.aim = Aim()
        #adiciona as variaveis aos grupos de controle usados pelo gerenciador de fisica
        for player in self.world.players:
            self.gravityObjects.append(player)
        #gerenciador de fisica do jogo
        self.physManager = PhysicManager()
        self.turnManager = TurnManager(self.world.players)
        #tiro
        self.shot = None
        self.playerUI = PlayerUI(self.maxLife,len(self.world.players),janela)
        return

    def update(self,deltaT,keyboard):
        self.turnManager.actualPlayer.update(keyboard,deltaT)
        #parte dedicada a atualizacaoo da fisica
        for player in self.turnManager.players:
            self.physManager.collisionPlayerVSBricks(player,self.world.mapMan.bricks)#colisao entre players e blocos
        self.physManager.gravity(deltaT, self.gravityObjects)#aplica a gravidade
        if self.turnManager.actualPlayer.jumpForce != 0:
            self.physManager.applyJump(deltaT, self.turnManager.actualPlayer)#faz o calculo do pulo do player atual
        if self.turnManager.actualPlayer.canShot == True:#caso o player possa atirar
            self.turnManager.actualPlayer.canShot = False
            self.createShot()
        if self.shot == None:
            self.physManager.playerMove(deltaT, self.turnManager.actualPlayer)#movimento do player
        else:
            self.physManager.shotMove(self.shot,deltaT)
            if self.physManager.collisionPlayerVSBall(self.turnManager.players,self.shot):
                self.shot.destroy = True
            self.physManager.collisionBallVsBrick(self.shot,self.world.mapMan.bricks)
            self.destroyShot()#destroi o tiro
        #--------------------------------------
        self.aim.update(self.turnManager.actualPlayer)#a mira segue o jogador
        self.playerUI.update(self.world.players)
        for playerID in range(len(self.world.players)):
            if self.world.players[playerID].life == 0:
                return "GO"+str((playerID + 1) % len(self.world.players))
        return

    def createShot(self):
        self.shot = Shot(self.aim)
        self.shot.forceX = self.turnManager.actualPlayer.shotForceX
        self.shot.forceY = self.turnManager.actualPlayer.shotForceY
        self.turnManager.actualPlayer.shotForceX = 0
        self.turnManager.actualPlayer.shotForceY = 0
        self.shot.direction = (self.turnManager.actualPlayer.shotDirectionX,self.turnManager.actualPlayer.shotDirectionY)
        self.gravityObjects.append(self.shot)
        return

        #desenha todos os blocos
    def draw(self):
        self.world.draw(self.turnManager)
        self.aim.draw()
        if self.shot != None:
            self.shot.draw()
        self.playerUI.draw(self.world.players)
        return

    def destroyShot(self):
        if self.shot.destroy or self.shot.x > 1280 or self.shot.x < 0 or self.shot.y > 720 or self.shot.y < 0:
            self.shot = None
            self.turnManager.changePlayer()
        return