__author__ = 'AlyssonGeraldo'
from PPlay.sound import *
class SoundManager():
    def __init__(self):
        self.shot = Sound("cannon.ogg")
        self.destroy = Sound("explosion.ogg")
        return

    def playSound(self,sound):
        if sound == "shot":
            self.shot.play()
        elif sound == "explosion":
            self.destroy.play()
        return
