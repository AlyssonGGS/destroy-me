__author__ = 'AlyssonNote'
from PPlay.gameobject import *
class DynamicGameObject(GameObject):
    def _init_(self):
        GameObject.__init__(self)
        self.gravity = 100
        return