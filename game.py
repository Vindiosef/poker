from Engine.round_manager import RoundManager
from Engine.table import Table
from Engine.player import Player

game = RoundManager()
table = Table()
for num in range(0,3):
    table.seats.players.append(Player(f"Player{num}"))

game.start_new_round(table)

for player in table.seats.players:
    print(player.hole_card)