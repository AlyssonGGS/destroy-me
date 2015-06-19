__author__ = 'AlyssonGeraldo'
class TurnManager():

    def __init__(self,players):
        self.players = players
        self.turn = 0
        self.actualPlayer = players[0]
        self.othersPlayers = []
        self.changeOtherPlayers()
        return

    def changePlayer(self):
        self.turn += 1#acrescenta o turno
        self.actualPlayer = self.players[self.turn%len(self.players)]# de acordo com o resto da divisao pelo numero total de players, seleciona o player atual
        self.changeOtherPlayers()#seleciona os outros jogadores
        return

    def changeOtherPlayers(self):
        self.othersPlayers = []
        for i in range(len(self.players)):
            if i != self.turn%len(self.players):
               self.othersPlayers.append(self.players[i])
        print(self.othersPlayers)
        return
