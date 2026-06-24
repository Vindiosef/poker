class Player:

    def __init__(self, name = None, initial_stack = None):
        self.name = name
        self.stack = initial_stack
        self.hole_card = []

    def add_holecard(self,cards):
        self.hole_card = cards

    def clear_holecard(self):
        self.hole_card = []