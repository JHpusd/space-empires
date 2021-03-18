import sys
sys.path.append('game_data/game_level_0_3')
from game_class import *
from player_classes import *

players = [CustomPlayer(), CustomPlayer()]
game = Game(players)
game.run_to_completion()
