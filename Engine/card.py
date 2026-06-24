class Card:

    CLUB = 1
    DIAMOND = 2
    HEART = 3
    SPADE = 4

    SUIT_MAP = {
        1 : 'C',
        2 : 'D',
        3 : 'H',
        4 : 'S'
    }

    RANK_MAP = {
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : '10',
        11 : 'J',
        12 : 'Q',
        13 : 'K',
        14 : 'A'
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = 14 if rank == 1 else rank
    
    def __eq__(self, value):
        return self.suit == value.suit and self.rank == value.rank
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        suit = self.SUIT_MAP[self.suit]
        rank = self.RANK_MAP[self.rank]
        return f"{suit},{rank}"
    
    def to_id(self):
        rank = 1 if self.rank == 14 else self.rank
        return rank + 13 * self.suit
    
    @classmethod
    def from_id(cls, card_id):
        suit = (card_id - 1) // 13 + 1
        rank = (card_id -1) % 13 + 1
        return cls(suit,rank)