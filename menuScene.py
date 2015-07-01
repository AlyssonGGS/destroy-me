__author__ = 'AlyssonGeraldo'
from scene import *
from PPlay.gameimage import *
class MenuScene(Scene):
    def __init__(self,janela):
        self.bg = GameImage("menu.png")
        self.possibleScenes = ["GAME","CREDITS"]
        self.game = GameImage("game.png")
        self.credits = GameImage("credits.png")
        self.sceneID = 0
        self.nextScene = self.possibleScenes[abs(self.sceneID)%len(self.possibleScenes)]
        self.game.set_position(janela.width*0.5 - self.game.width/2,janela.height * 0.5 - self.game.height / 2)
        self.credits.set_position(janela.width*0.5 - self.credits.width/2,janela.height * 0.5 - self.credits.height / 2)
        self.changeScene = False
        return

    def update(self,dt,keyboard):
        if keyboard.key_pressed("RIGHT"):
            if not self.changeScene:
                self.sceneID += 1
            self.changeScene = True
        elif keyboard.key_pressed("LEFT"):
            if not self.changeScene:
                self.sceneID -= 1
            self.changeScene = True
        else:
            if self.changeScene:
                self.changeScene = False
                self.nextScene = self.possibleScenes[abs(self.sceneID)%len(self.possibleScenes)]
        if keyboard.key_pressed("ENTER"):
            print(self.nextScene)
            return self.nextScene
        return

    def draw(self):
        self.bg.draw()
        if self.nextScene == self.possibleScenes[0]:
            self.game.draw()
        elif self.nextScene == self.possibleScenes[1]:
            self.credits.draw()
        return
