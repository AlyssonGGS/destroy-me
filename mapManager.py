__author__ = 'AlyssonNote'
from brick import *
from random import randint

class MapManager():
    def __init__(self):
        #cria os blocos
        self.possiblePlayerPosition = []
        self.bricks = self.createBrick("map1")
        print(self.possiblePlayerPosition)
        return

    def createBrick(self,mapName):
        row = 0 # variavel que serve para colocar o bloco na altura certa
        auxBricks = [] # vetor que guardará os blocos criados a partir do arquivo de texto
        auxBrick = GameImage("brick.png") # auxiliar que guarda a largura e a altura da imagem do bloco
        BD = open(mapName)#começa a ler o arquivo
        self.linhaAtual = 0
        for line in BD:#percorre as linhas
            cels = line.split("\n")[0].split(' ') # separa os caracteres que serão interpretados pelo codigo
            auxBricks.append(self.processLine(cels,auxBrick,row))# interpreta a linha e gera uma fileira de blocos
            row += 1 # aumenta a altura dos blocos
        BD.close()#fecha o arquivo
        return auxBricks#retorna os blocos

    def processLine(self,lin,auxBric,h):
        #lin-> linha atual lida no metodo createBrick
        #auxBric-> imagem de referencia para altura e largura dos blocos
        #h-> é a altura da proxima linha
        bricks = [] # cria um auxiliar que guardara a linha atual
        for i in range(len(lin)):#percorre a linha
            if lin[i] == '1':# caso seja positivo
                bricks.append(Brick((auxBric.width * i),auxBric.height * h))#cria um bloco
            elif lin[i] == '2':
                self.possiblePlayerPosition.append(( i * 72, h * 64 ))
        return bricks#retorna os blocos da linha recem lida

    def draw(self):
        for i in range(len(self.bricks)):
            for j in range(len(self.bricks[i])):
                self.bricks[i][j].draw()
        return

    def getPlayerPosition(self,numPlayers):
        id = randint(0,numPlayers)
        position = self.possiblePlayerPosition[id]
        self.possiblePlayerPosition.pop(id)
        return position