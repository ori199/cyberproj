import pygame
import random

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Define the Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = 10

    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed

        # Remove the bullet when it goes off screen
        if self.rect.bottom < 0 or self.rect.top > screen_height or self.rect.right < 0 or self.rect.left > screen_width:
            self.kill()

# Set up the sprite groups
all_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

# Create the player
player = Player(screen_width/2, screen_height/2)
all_sprites.add(player)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a new bullet when the player presses spacebar
                bullet = Bullet(player.rect.centerx, player.rect.centery, random.choice(['up', 'down', 'left', 'right']))
                all_sprites.add(bullet)
                bullet_sprites.add(bullet)

    # Update the sprites
    all_sprites.update()
    bullet_sprites.update()

    # Draw the sprites
    screen.fill(black)
    all_sprites.draw(screen)

    # Check for collisions
    hits = pygame.sprite.groupcollide(bullet_sprites, all_sprites, True, False)
    for bullet, players in hits.items():
        for player in players:
            print("Player hit by bullet!")

    # Update the screen
    pygame.display.flip()

    # Limit the FPS
    clock.tick(60)

# Quit the game
pygame.quit()
