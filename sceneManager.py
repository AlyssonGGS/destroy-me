__author__ = 'AlyssonGeraldo'
from scene import *
from menuScene import *
from gameScene import *

class SceneManager():
    def __init__(self,janela):
        self.janela = janela
        self.actualScene = MenuScene(janela)
        return

    def update(self,dt,keyboard):
        newScene = self.actualScene.update(dt,keyboard)
        if newScene == "GAME":
            print("Ola")
            self.actualScene = GameScene(self.janela)
        return

    def draw(self):
        self.actualScene.draw()
        return