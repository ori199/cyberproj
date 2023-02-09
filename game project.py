import sys
import pygame

import random




pygame.display.init()
# Initialize the game
pygame.init()
radios=20
colorblue=(0,191,255)
def player(x,y):
    pygame.draw.circle(screen,colorblue,(x+radios,y+radios),radios,int(radios/4))
    pygame.draw.line(screen,colorblue,(x+radios-int(radios/10),y+2*radios),(x+radios-int(radios/10),y+6*radios),int(radios/4))
    #hands
    pygame.draw.line(screen,colorblue,(x+radios-int(radios/10),y+2*radios),((x+radios-int(radios/10))-radios,y+4*radios),int(radios/4))
    pygame.draw.line(screen, colorblue, (x + radios - int(radios / 10), y + 2 * radios),((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    #legs
    pygame.draw.line(screen, colorblue, (x + radios - int(radios / 10), y + 6 * radios), ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(screen, colorblue, (x + radios - int(radios / 10), y + 6 * radios),((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))
colorred = (255,0,0)
gun_color = pygame.Color("grey")
def eenemy(x,y):
    pygame.draw.circle(screen,colorred,(x+radios,y+radios),radios,int(radios/4))
    pygame.draw.line(screen,colorred,(x+radios-int(radios/10),y+2*radios),(x+radios-int(radios/10),y+6*radios),int(radios/4))
    #hands
    pygame.draw.line(screen,colorred,(x+radios-int(radios/10),y+2*radios),((x+radios-int(radios/10))-radios,y+4*radios),int(radios/4))
    pygame.draw.line(screen, colorred, (x + radios - int(radios / 10), y + 2 * radios),((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    #legs
    pygame.draw.line(screen, colorred, (x + radios - int(radios / 10), y + 6 * radios), ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(screen, colorred, (x + radios - int(radios / 10), y + 6 * radios),((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))

    def castle(x, y):
        pygame.draw.rect(screen, (0, 0, 255),
                         [x, y, radios * 4, radios * 5], 2)
# Set the window size
def draw_gun(x, y):
    # Draw the gun handle
    pygame.draw.rect(screen, gun_color, (x - 20, y + 20, 40, 10))
    pygame.draw.rect(screen, gun_color, (x - 15, y + 30, 30, 10))

    # Draw the gun barrel
    barrel_start = (x, y)
    barrel_end = (x, y - 40)
    barrel_width = 10
    pygame.draw.line(screen, gun_color, barrel_start, barrel_end, barrel_width)
    pygame.draw.circle(screen, gun_color, (x, y - 40), int(barrel_width / 2))

    # Draw the gun sight
    sight_radius = 5
    sight_center = (x, y - 20)
    pygame.draw.circle(screen, pygame.Color("red"), sight_center, sight_radius)



WIDTH = 1920
HEIGHT = 1080

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Load the castle image
castle_image = pygame.image.load("castle.png")

# Set the castle location
castle_x = 0
castle_y = HEIGHT - castle_image.get_height()

# Load the player image
player_image = pygame.image.load("player.png")

# Set the player location
player_x = WIDTH / 2
player_y = HEIGHT - castle_image.get_height() - 50

# Set player speed
player_speed = 5

# Load the enemy image
# Create the enemies
enemies = []
for i in range(5):
    x = random.randint(0, WIDTH-50)
    y = random.randint(0, HEIGHT-castle_image.get_height()-50)
    enemies.append([x, y])

# Set the gun image
gun_image = pygame.image.load("gun.png")

# Set the gun location
gun_x = player_x
gun_y = player_y

# Set the gun speed
gun_speed = 20

# Set the score
score = 0

# Load the font for displaying the score
font = pygame.font.Font(None, 30)

# Load the game over image
game_over_image = pygame.image.load("game_over.png")

# Load the game over sound effect
game_over_sound = pygame.mixer.Sound("game_over.wav")

# Load the main menu image
main_menu_image = pygame.image.load("main_menu.png")

# Set the game state
game_state = "main_menu"

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= player_speed
            elif event.key == pygame.K_DOWN:
                player_y += player_speed
            elif event.key == pygame.K_SPACE:
                gun_x = player_x
                gun_y = player_y

    # Update the gun position
    gun_y -= gun_speed

    # Check if the gun hit an enemy
    for enemy in enemies:
        if (gun_x >= enemy[0] and gun_x <= enemy[0] + 50) and (gun_y >= enemy[1] and gun_y <= enemy[1] + 50):
            score += 1
            enemies.remove(enemy)
            break

    # Check if player is still in the game window
    if player_y < HEIGHT - castle_image.get_height() - 50:
        player_y = HEIGHT - castle_image.get_height() - 50

    # Check if game is over
    if len(enemies) == 0:
        game_state = "game_over"
        pygame.mixer.music.stop()
        game_over_sound.play()

    # Draw the castle
    screen.blit(castle_image, (castle_x, castle_y))

    # Draw the player
    player(player_x, player_y)

    # Draw the gun
    screen.blit(gun_image, (gun_x, gun_y))

    # Draw the enemies
    for enemy in enemies:
        eenemy(enemy[0], enemy[1])

    # Draw the score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the game loop speed
    pygame.time.wait(30)

    # Quit the game
    pygame.quit()