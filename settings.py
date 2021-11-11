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