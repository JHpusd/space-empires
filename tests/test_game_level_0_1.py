import sys
sys.path.append('game_data/game_level_0_1')
from game_class import *
from player_classes import *

# test A
players = [CustomPlayer(), CustomPlayer()]
game = Game(players)

game.complete_move_phase()
game.complete_combat_phase()
game.complete_move_phase()
game.complete_combat_phase()
game.complete_move_phase()
game.complete_combat_phase()
print(game.state['players'])

# test B
num_wins = {1: 0, 2: 0}
for _ in range(200):
    players = [CustomPlayer(), CustomPlayer()]
    game = Game(players)
    game.run_to_completion()
    winner = game.state['winner']
    num_wins[winner] += 1
print(num_wins)
if abs(num_wins[1] - num_wins[2]) > 40:
    print("there is a problem")
