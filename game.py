__author__ = 'AlyssonNote'
from PPlay.window import *
from gameScene import *

janela = Window(1280,720)
actualScene = GameScene()
while True:
    #roda o update da cena atual
    actualScene.update(janela.delta_time(),janela.get_keyboard())
    #desenha a cena
    janela.set_background_color((255,255,255))
    actualScene.draw()
    #atualiza a janela
    janela.update()