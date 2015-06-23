__author__ = 'AlyssonNote'
from gameScene import *
from PPlay.window import *

window = Window(1280,720)
actualScene = GameScene(window)
while True:
    #roda o update da cena atual
    actualScene.update(window.delta_time(),window.get_keyboard())
    #desenha a cena
    window.set_background_color((255,255,255))
    actualScene.draw()
    #atualiza a janela
    window.update()
