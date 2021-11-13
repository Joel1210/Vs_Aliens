class Settings:
    '''A class to store all settings for Alien Invasion'''
    def __init__(self):
        '''Initialize the game's settings'''
        #screen settings
        self.screen_width = 900
        self.screen_height = 600
        #light gray background color
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_speed = 1.5

        #Bullet Settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        #dark gray color
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3