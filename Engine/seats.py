from Engine.player import Player

class Seats:

    def __init__(self):
        self.players = []

    def sitdown(self, player):
        self.players.append(player)
    
    def size(self):
        return len(self.players)