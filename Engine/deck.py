from Engine.card import Card
import random

class Deck:

    def __init__(self, deck_ids = None):
        #this allows for deck variations
        self.deck = [Card.from_id(cid) for cid in deck_ids] if deck_ids else self._setup_52_cards()

    def draw_card(self):
        return self.deck.pop()

    def draw_cards(self, num):
        return [self.draw_card() for _ in range(num)]
    
    def shuffle(self):
        random.shuffle(self.deck)

    def _setup_52_cards(self):
        return [Card.from_id(cid) for cid in range (1,53)]