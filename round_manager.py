from player import Player
from table import Table
from seats import Seats

class RoundManager:

    @classmethod
    def start_new_round(self, table):
        table.deck.shuffle()
        self._deal_holecard(table.deck)

    @classmethod
    def _deal_holecard(self, deck, players):
        for player in players:
            player.add_holecard(deck.draw_cards(2))
