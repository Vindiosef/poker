from Engine.card import Card
from Engine.deck import Deck
from Engine.seats import Seats

class Table:
    
    def __init__(self):
        self._community_card = []
        self.deck = Deck()
        self.seats = Seats()

    def add_community_card(self, card):
        if len(self._community_card) == 5:
            raise ValueError()
        self._community_card.append(card)
