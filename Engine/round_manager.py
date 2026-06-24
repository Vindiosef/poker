from Engine.player import Player
from Engine.table import Table
from Engine.seats import Seats
from Engine.deck import Deck

class RoundManager:

    @classmethod
    def start_new_round(self, table):
        table.deck.shuffle()
        self._deal_holecard(table.deck, table.seats.players)

    @classmethod
    def _deal_holecard(self, deck, players):
        for player in players:
            player.add_holecard(deck.draw_cards(2))

