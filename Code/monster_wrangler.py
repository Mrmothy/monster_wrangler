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
        self.frame_count += 1
        if self.frame_count == FPS:
            self.round_time += 1
            self.frame_count = 0

        #Check for collisions
        self.check_collisions()

    def draw(self):
        """Draw the hud and other to the display"""
        #Set Colors
        WHITE = (225, 225, 255)
        BLUE = (20, 176, 235)
        GREEN = (87, 201, 47)
        PURPLE = (226, 73, 243)
        YELLOW = (243, 157, 20)
        
        #Add monster colors to a list where the index of the color matches target_monster_images
        colors = [BLUE, GREEN, PURPLE, YELLOW]

        #Set Text
        catch_text = self.font.render("Current Catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH / 2
        catch_rect.top = 5

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render(f"Rounds: {self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render(f"Round Time: {self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render(f"Warps: {self.player.warps}", True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH -10, 35)

        #! This is an after thought add
        game_title_text = self.font.render("MONSTER WRANGLER", True, WHITE)
        game_title_rect = game_title_text.get_rect()
        game_title_rect.topright = (WINDOW_WIDTH - 10, 65)

        #Blit the HUD
        display_surface.blit(catch_text, catch_rect)
        display_surface.blit(score_text, score_rect)
        display_surface.blit(lives_text, lives_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)
        display_surface.blit(warp_text, warp_rect)
        display_surface.blit(game_title_text, game_title_rect) #! This is an after thought add
        display_surface.blit(self.target_monster_image, self.target_monster_rect)
        
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (WINDOW_WIDTH / 2 - 32, 30, 64, 64), 2)
        pygame.draw.rect(display_surface, colors[self.target_monster_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT - 200), 4)

    def check_collisions(self):
        """Check for collisions between players and monsters"""
        #Check for collision between a player and an individual monster
        #We must test the type of the monster to see if it matches the type of our target monster.
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        
        #We collided with a monster
        if collided_monster:
            #Caught the correct monster
            if collided_monster.type == self.target_monster_type:
                self.score += 100 * self.round_number
                #Remove caught monster
                collided_monster.remove(self.monster_group)
                if (self.monster_group):
                    #There are more monsters to catch
                    self.player.catch_sound.play()
                    self.chose_new_target()
                else:
                    #The round is complete
                    self.player.reset()
                    self.start_new_round()
                    self.next_level_sound.play() #!Might be wrong location
            #Caught wrong monster
            else:
                self.player.die_sound.play()
                self.player.lives -= 1
                #Check for game over
                if self.player.lives == 0:
                    self.pause_game()
                    self.rest_game()
                self.player.reset()

    def start_new_round(self):
        """Populate board with new monsters"""
        #
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