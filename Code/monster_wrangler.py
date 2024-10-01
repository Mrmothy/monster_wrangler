import pygame, random
from os.path import join


#Initialize Pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")


#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()


class Game():
    """A class to control gameplay"""
    def __init__(self, player, monster_group):
        """Initialize the game object"""
        #Set Game Values
        self.score = 0
        self.round_number = 0

        self.round_time = 0
        self.frame_count = 0

        self.player = player
        self.monster_group = monster_group

        #Set Sounds and Music
        self.next_level_sound = pygame.mixer.Sound(join("Assets", "next_level.wav"))

        #Set Font
        self.font = pygame.font.Font(join("Assets", "Abrushow.ttf"), 24)

        #Set Images
        blue_image = pygame.image.load(join("Assets", "blue_monster.png")).convert_alpha()
        green_image = pygame.image.load(join("Assets", "blue_monster.png")).convert_alpha()
        purple_image = pygame.image.load(join("Assets", "purple_monster.png")).convert_alpha()
        yellow_image = pygame.image.load(join("Assets", "yellow_monster.png")).convert_alpha()
        #This list corresponds to the monster_type attribute.
        #Monster type is an int 0 -> Blue, 1 -> Green, 2 -> Purple, 3 -> Yellow.
        self.target_monster_images = [blue_image, green_image, purple_image, yellow_image]

        self.target_monster_type = random.randint(0,3)
        self.target_monster_image = self.target_monster_images[self.target_monster_type]

        self.target_monster_rect = self.target_monster_image.get_rect()
        self.target_monster_rect.centerx = WINDOW_WIDTH / 2
        self.target_monster_rect.top = 30

    def update(self):
        """Update our game object"""
        pass

    def draw(self):
        """Draw the hud and other to the display"""
        pass

    def check_collisions(self):
        """Check for collisions between players and monsters"""
        pass

    def start_new_round(self):
        """Populate board with new monsters"""
        pass

    def chose_new_target(self):
        """Choose a new target monster for the player"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def rest_game(self):
        """Rest the game"""
        pass

class Player(pygame.sprite.Sprite):
    """A player class that the user can control"""
    def __init__(self):
        """Initialize the player"""
        super().__init__()
        self.image = pygame.image.load(join('Assets', 'knight.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = (WINDOW_WIDTH / 2)
        self.rect.bottom = (WINDOW_HEIGHT)

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.catch_sound = pygame.mixer.Sound(join('Assets', 'catch.wav'))
        self.die_sound = pygame.mixer.Sound(join('Assets', 'die.wav'))
        self.warp_sound = pygame.mixer.Sound(join('Assets', 'warp.wav'))

    def update(self):
        """Update the player"""
        keys = pygame.key.get_pressed()

        #Move the player within the bounds of the screen 
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += self.velocity

    def warp(self):
        """Warp the player to safe zone"""
        if self.warps > 0:
            self.warps - 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def resets_player(self):
        """Rests the player to starting position"""
        self.rect.centerx = WINDOW_WIDTH / 2
        self.rect.bottom = WINDOW_HEIGHT

class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""
    def __init__(self, x, y, image, monster_type):
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        #Monster type is an int 0 -> Blue, 1 -> Green, 2 -> Purple, 3 -> Yellow.
        self.type = monster_type

        #Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)
        

    def update(self):
        """Update the monster"""
        self.rect.x += self.dx*self.velocity
        self.rect.y += self.dy*self.velocity

        #Bounce the monster off the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1 * self.dx
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.dy = -1 * self.dy

#Create a Player group and Player object
my_player_group = pygame.sprite.Group()
my_player = Player()
my_player_group.add(my_player)

#Create a Monster group.
my_monster_group = pygame.sprite.Group()
#! Test monster
monster = Monster(500, 500, pygame.image.load('Assets/green_monster.png'), 1)
my_monster_group.add(monster)
monster = Monster(100, 500, pygame.image.load('Assets/blue_monster.png'), 1)
my_monster_group.add(monster)

#Create a Game Object
my_game = Game(my_player, my_monster_group)


#*Start game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Fill display
    display_surface.fill((0, 0, 0))

    #Update and draw sprite group
    my_player_group.update()
    my_player_group.draw(display_surface)

    my_monster_group.update()
    my_monster_group.draw(display_surface)

    #Update and draw the Game
    my_game.update()
    my_game.draw()

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#*End game loop
pygame.quit()