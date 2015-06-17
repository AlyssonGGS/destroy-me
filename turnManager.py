__author__ = 'AlyssonGeraldo'
class TurnManager():

    def __init__(self,players):
        self.players = players
        self.turn = 0
        self.actualPlayer = players[0]
        return

    def changePlayer(self):
        self.turn += 1
        self.actualPlayer = self.players[self.turn%len(self.players)]
        return