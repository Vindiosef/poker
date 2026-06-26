from Engine.player import Player
from Engine.table import Table
from Engine.seats import Seats
from Engine.deck import Deck

class RoundManager:

    @classmethod
    def start_new_round(self, table):
        table.deck.shuffle()
        self._deal_holecard(table.deck, table.seats.players)

    def flop(self,table):
        table.deck.draw_card()
        for card in table.deck.draw_cards(3):
            table.add_community_card(card)
        print(table._community_card)

    def turn(self,table):
        table.deck.draw_card()
        for card in table.deck.draw_cards(1):
            table.add_community_card(card)       
        print(table._community_card)
    
    def river(self,table):
        table.deck.draw_card()
        for card in table.deck.draw_cards(1):
            table.add_community_card(card)
        print(table._community_card)

    @classmethod
    def _deal_holecard(self, deck, players):
        for player in players:
            player.add_holecard(deck.draw_cards(2))

