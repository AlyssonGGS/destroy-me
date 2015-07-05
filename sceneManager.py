__author__ = 'AlyssonGeraldo'
from scene import *
from menuScene import *
from gameScene import *
from gameOverScene import *

class SceneManager():
    def __init__(self,janela):
        self.janela = janela
        self.actualScene = MenuScene(janela)
        return

    def update(self,dt,keyboard):
        newScene = self.actualScene.update(dt,keyboard)
        if newScene != None:
            if newScene == "GAME":
                print("Ola")
                self.actualScene = GameScene(self.janela)
            elif newScene.startswith("GO"):
                newScene = newScene.replace("GO","")
                self.actualScene = GameOverScene(self.janela,int(newScene))
            elif newScene == "CLOSE":
                self.janela.close()
            elif newScene == "MENU":
                self.actualScene = MenuScene(self.janela)
        return

    def draw(self):
        self.actualScene.draw()
        return