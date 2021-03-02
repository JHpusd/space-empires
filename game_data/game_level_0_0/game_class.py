class Game:
    def __init__(self, players, board_size=[7,7]):
        self.players = players
        self.set_player_numbers()

        board_x, board_y = board_size
        mid_x = (board_x + 1) // 2
        mid_y = (board_y + 1) // 2

        self.state = {
            'turn': 1,
            'board_size': board_size,
            'players': {
                1: {
                    'scout_coords': (mid_x, 1),
                    'home_colony_coords': (mid_x, 1)
                },
                2: {
                    'scout_coords': (mid_x, board_y),
                    'home_colony_coords': (mid_x, board_y)
                }
            },
            'winner': None
        }
    
    def set_player_numbers(self):
        for i,player in enumerate(self.players):
            player.set_player_number(i+1)

    def check_if_coords_are_in_bounds(self, coords):
        x, y = coords
        board_x, board_y = self.state['board_size']
        if 1 <= x and x <= board_x:
            if 1 <= y and y <= board_y:
                return True
        return False

    def check_if_translation_is_in_bounds(self, coords, translation):
        max_x, max_y = self.state['board_size']
        x, y = coords
        dx, dy = translation
        new_coords = (x+dx,y+dy)
        return self.check_if_coords_are_in_bounds(new_coords)

    def get_in_bounds_translations(self, coords):
        translations = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]
        in_bounds_translations = []
        for translation in translations:
            if self.check_if_translation_is_in_bounds(coords, translation):
                in_bounds_translations.append(translation)
        return in_bounds_translations

    def complete_turn(self):
        for player_num in self.state['players']:
            init_coord = self.state['players'][player_num]['scout_coords']
            choices = self.get_in_bounds_translations(init_coord)
            for player in self.players:
                if player.player_number == player_num:
                    move = player.choose_translation(self.state, choices)
            new_coords = (init_coord[0]+move[0], init_coord[1]+move[1])
            self.state['players'][player_num]['scout_coords'] = new_coords
        self.state['turn'] += 1
        self.state['winner'] = self.check_for_winner()

    def run_to_completion(self):
        while self.state['winner'] == None:
            self.complete_turn()

    def check_for_winner(self):
        player_1 = self.state['players'][1]
        player_1_scout = player_1['scout_coords']
        player_1_base = player_1['home_colony_coords']
        player_2 = self.state['players'][2]
        player_2_scout = player_2['scout_coords']
        player_2_base = player_2['home_colony_coords']

        if player_1_scout != player_2_base and player_2_scout != player_1_base:
            return None
        if player_1_scout == player_2_base and player_2_scout != player_1_base:
            return 1
        if player_1_scout != player_2_base and player_2_scout==player_1_base:
            return 2
        if player_1_scout == player_2_base and player_2_scout == player_1_base:
            return "Tie"
