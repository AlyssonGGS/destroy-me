__author__ = 'AlyssonNote'
from PPlay.window import *
from sceneManager import *
window = Window(1280,720)
sceneManager = SceneManager(window)
while True:
    #roda o update da cena atual
    sceneManager.update(window.delta_time(),window.get_keyboard())
    #desenha a cena
    window.set_background_color((255,255,255))
    sceneManager.draw()
    #atualiza a janela
    window.update()
