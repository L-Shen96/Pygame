class Settings():

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_size = 30
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, else left
        # self.fleet_direction = 1

        # Speed up rate
        self.speedup_rate = 1.2

        self.initialize_dynamic_settings()

        # Increase alien point values
        self.score_scale = 1.5

        # Scoring
        self.alien_points = 50

        # score_path
        self.path = 'high_score.txt'

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 4.5
        self.alien_speed_factor = 1.5
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        # Increase speed settings
        self.ship_speed_factor *= self.speedup_rate
        self.bullet_speed_factor *= self.speedup_rate
        self.alien_speed_factor *= self.speedup_rate

        self.alien_points *= self.score_scale
        self.alien_points = int(self.alien_points)
