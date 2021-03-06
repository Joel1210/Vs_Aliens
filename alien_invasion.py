import sys, pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
# print(pygame.ver)

class AlienInvasion:
    '''Overall class to manage game assets and behavior'''

    def __init__(self):
        '''Initialize the game, and create game resources'''
        pygame.init()
        self.settings = Settings()

        #For windowed mode. 900x600
        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)       
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''Start the main loop for the game'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
        
    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''Respond to the keypresses'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #Press Esc to quit the game
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        '''Respond to key releases'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        
        #if statement to limit the amount of bullets on screen.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update the position of bullets & get rid of the ones that go beyond screen'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #Checking to see if the bullets were properly deleted
        # print(len(self.bullets))??????

    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen'''
        #Redraw the screen during each pass through the loop.
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Make the most recently drawn screen visible.
        pygame.display.flip()
  
if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()