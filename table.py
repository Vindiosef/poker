from card import Card
from deck import Deck

class Table:
    
    def __init__(self):
        self._community_card = []
        self.deck = Deck()

    def add_community_card(self, card):
        if len(self._community_card) == 5:
            raise ValueError()
        self._community_card.append(card)
