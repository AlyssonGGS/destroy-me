__author__ = 'AlyssonGeraldo'
from scene import *
from PPlay.gameimage import *

class GameOverScene(Scene):
    def __init__(self,janela,winner):
        self.bg = GameImage("gameover.png")
        self.win = GameImage("win"+str(winner + 1)+".png")
        self.win.set_position(0,janela.height / 2 - self.win.height / 2)
        return

    def update(self,deltaT,keyboard):
        if keyboard.key_pressed("ESC"):
            return "CLOSE"
        elif keyboard.key_pressed("RETURN"):
            return "MENU"
        return

    def draw(self):
        self.bg.draw()
        self.win.draw()
        return