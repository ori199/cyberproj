import time

import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
game_screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Multiplayer Shooter")

# Set up the game clock
clock = pygame.time.Clock()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

blue_wall = pygame.image.load('wallv3.png').convert()


# Load the player images
imp = pygame.image.load("spaceshipv2.png").convert()
spaceship_up = pygame.transform.scale(imp, (50, 50))
spaceship_down = pygame.transform.rotate(spaceship_up, 180)
spaceship_left = pygame.transform.rotate(spaceship_up, 90)
spaceship_right = pygame.transform.rotate(spaceship_up, 270)


# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, player_number, start_x, start_y, facing_right_image, facing_left_image, facing_up_image,
                 facing_down_image, surface):
        super().__init__()
        self.direction = "right"
        self.player_number = player_number
        self.image = facing_right_image
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.speed = 5
        self.hp = 5
        self.is_alive = True
        self.facing_right_image = facing_right_image
        self.facing_left_image = facing_left_image
        self.facing_up_image = facing_up_image
        self.facing_down_image = facing_down_image
        self.bullet_group = pygame.sprite.Group()
        self.surface = surface
        self.lastshottime = time.time()

    def update(self, keys_pressed, wall_list):
        # Move the player based on the keys pressed
        if self.player_number == 1:
            if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = "left"
                self.image = self.facing_left_image
            if keys_pressed[pygame.K_RIGHT] and self.rect.right < screen_width:
                self.rect.x += self.speed
                self.direction = "right"
                self.image = self.facing_right_image
            if keys_pressed[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.speed
                self.direction = "up"
                self.image = self.facing_up_image
            if keys_pressed[pygame.K_DOWN] and self.rect.bottom < screen_height:
                self.rect.y += self.speed
                self.direction = "down"
                self.image = self.facing_down_image
            if keys_pressed[pygame.K_KP0] and self.rect.left > 0:
                self.shoot()
        if self.player_number == 2:
            if keys_pressed[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
                self.direction = "left"
                self.image = self.facing_left_image
            if keys_pressed[pygame.K_d] and self.rect.right < screen_width:
                self.rect.x += self.speed
                self.direction = "right"
                self.image = self.facing_right_image
            if keys_pressed[pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
                self.direction = "up"
                self.image = self.facing_up_image
            if keys_pressed[pygame.K_s] and self.rect.bottom < screen_height:
                self.rect.y += self.speed
                self.direction = "down"
                self.image = self.facing_down_image
            if keys_pressed[pygame.K_SPACE]:
                self.shoot()

        # Check if the player collides with any wall
        for wall in wall_list:
            if self.rect.colliderect(wall.rect):
                # If the player collides with the wall, move them back to their previous position
                if self.direction == "right":
                    self.rect.right = wall.rect.left
                elif self.direction == "left":
                    self.rect.left = wall.rect.right
                elif self.direction == "up":
                    self.rect.top = wall.rect.bottom
                else:
                    self.rect.bottom = wall.rect.top

        # Check if the player is still on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


    def shoot(self):
        if time.time() - self.lastshottime >= 1:
            self.lastshottime = time.time()
            if self.direction == "right":
                x, y = self.rect.midright
            elif self.direction == "left":
                x, y = self.rect.midleft
            elif self.direction == "up":
                x, y = self.rect.midtop
            else:
                x, y = self.rect.midbottom
            new_bullet = Bullet(x, y, self.direction, self.player_number)
            all_bullets.add(new_bullet)

    def take_damage(self):
        self.hp -= 1
        if self.hp == 0:
            self.remove(all_players)
            
    def check_collision_with_bullet(self, bullett):
        if bullett.player_number != self.player_number:
            if self.rect.collidepoint(bullett.rect.center):
                self.take_damage()
                bullett.kill()



    # def check_collision_with_wall(self, walls):
    #     for wall in walls:
    #         if self.rect.colliderect(wall.rect):
    #             if self.rect.top < wall.rect.bottom and self.rect.right > wall.rect.left:
    #                 self.rect.top = wall.rect.bottom
    #             elif self.rect.bottom > wall.rect.top and self.rect.right > wall.rect.left:
    #                 self.rect.bottom = wall.rect.top
    #             elif self.rect.left < wall.rect.right and self.rect.bottom > wall.rect.top:
    #                 self.rect.left = wall.rect.right
    #             elif self.rect.right > wall.rect.left and self.rect.bottom > wall.rect.top:
    #                 self.rect.right = wall.rect.left

    # def check_colision_with_wall(self, walllist):
    #     for wall in walllist:
    #         if self.rect.collidepoint(wall.rect.center):

            # posright = (wall.rect.right, self.rect.y)
            # posleft = (wall.rect.left, self.rect.y)
            # postop = (self.rect.x, wall.rect.top)
            # posleft = (self.rect.x, wall.rect.top)
            #
            # if self.rect.collidepoint(posright):
            #     self.rect.x = wall.rect.right
            # if self.rect.collidepoint(posleft):
            #     self.rect.x = wall.rect.left
            # if self.rect.collidepoint(postop):
            #     self.rect.x = wall.rect.bottom
            # if self.rect.collidepoint(posleft):
            #     self.rect.x = wall.rect.top




# Define the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, player_number):
        super().__init__()
        self.player_number = player_number
        self.image = pygame.Surface((2, 2))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
        self.direction = direction

    def update(self):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

        # Remove the bullet if it goes off the screen
        if self.rect.right < 0 or self.rect.left > screen_width or self.rect.bottom < 0 or self.rect.top > screen_height:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



blue_wall = pygame.transform.scale(blue_wall, (300, 50))
wall_blue_left = pygame.transform.rotate(blue_wall,90)
wall_group = pygame.sprite.Group()
for i in range(1):
    new_wall1 = Wall(random.randrange(0, screen_width-300), random.randrange(0, screen_height-50), wall_blue_left)
    new_wall2 = Wall(random.randrange(0, screen_width - 300), random.randrange(0, screen_height - 50), blue_wall)
    wall_group.add(new_wall1)
    wall_group.add(new_wall2)

def healthcounter(player_list):
    for p in player_list:
        hp_text = (pygame.font.Font(None, 30)).render("player" + str(p.player_number) + ": " + str(p.hp), True,
                                                    (255, 255, 255))
        game_screen.blit(hp_text, (p.player_number * 200, 10))


# Create the player sprites
player1 = Player(1, 100, 150, spaceship_right, spaceship_left, spaceship_up, spaceship_down, game_screen)
player2 = Player(2, 200, 150, spaceship_right, spaceship_left, spaceship_up, spaceship_down, game_screen)
all_players = pygame.sprite.Group(player1, player2)

# Create the bullet sprite group
all_bullets = pygame.sprite.Group()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    game_screen.fill(BLACK)
    healthcounter(all_players.sprites())
    all_players.update(keys, wall_group.sprites())
    all_bullets.update()
    # draws all players
    all_players.draw(game_screen)
    # draws all bullets
    all_bullets.draw(game_screen)
    # checks collisions with all the players
    wall_group.draw(game_screen)
    for player in all_players.sprites():
        for bullet in all_bullets.sprites():
            player.check_collision_with_bullet(bullet)
    # for player in all_players.sprites():
    #     player.check_collision_with_wall(wall_group.sprites())

    # for player in all_players.sprites():
    #     player.check_colision_with_wall(wall_group.sprites())
    # shows players hp on the screen
    pygame.display.update()
    clock.tick(60)
pygame.quit()
