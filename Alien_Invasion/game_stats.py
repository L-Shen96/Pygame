class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # High score
        self.path = ai_settings.path
        self.get_high_score()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit

        self.score = 0

        self.level = 1

    def get_high_score(self):
        with open(self.path, 'r') as f:
            high_score = f.read()
            f.close()
        self.high_score = int(high_score)


