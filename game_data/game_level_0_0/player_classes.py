from random import random
import math

def calc_distance(start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return math.sqrt(dx**2 + dy**2)

class RandomPlayer():
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def choose_translation(self, game_state, choices):
        random_idx = math.floor(len(choices) * random())
        return choices[random_idx]

class CustomPlayer():
    def __init__(self):
        self.player_number = None

    def set_player_number(self, n):
        self.player_number = n

    def get_opponent_player_number(self):
        if self.player_number == None:
            return None
        elif self.player_number == 1:
            return 2
        elif self.player_number == 2:
            return 1

    def choose_translation(self, game_state, choices):
        myself = game_state['players'][self.player_number]
        opponent_player_number = self.get_opponent_player_number()
        opponent = game_state['players'][opponent_player_number]

        my_scout_coords = myself['scout_coords']
        opponent_home_coords = opponent['home_colony_coords']

        smallest_translation = choices[0]
        small_x = my_scout_coords[0] + smallest_translation[0]
        small_y = my_scout_coords[1] + smallest_translation[1]
        smallest_distance_coord = (small_x, small_y)
        smallest_distance = calc_distance(smallest_distance_coord, opponent_home_coords)

        for translation in choices:
            new_x = my_scout_coords[0] + translation[0]
            new_y = my_scout_coords[1] + translation[1]
            new_coords = (new_x, new_y)
            if calc_distance(new_coords, opponent_home_coords) < smallest_distance:
                smallest_translation = translation
                smallest_distance = calc_distance(new_coords, opponent_home_coords)
        
        return smallest_translation
