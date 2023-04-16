import pygame
import math

pygame.init()

# Set up the display
screen = pygame.display.set_mode((500, 500))

# Load the image for the player
player_image = pygame.image.load("spaceshipv2.png")
player_image = pygame.transform.scale(player_image,(50,50))
player_rect = player_image.get_rect()
player_rect.center = (250, 250)

# Set up the bullet
bullet_image = pygame.image.load("bullet.png")
bullet_image = pygame.transform.scale(bullet_image,(2,4))
bullet_rect = bullet_image.get_rect()
bullet_speed = 10
bullet_heading = 0
last_shot_time = 0  # variable to keep track of time since last shot

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.move_ip(-10, 0)
            elif event.key == pygame.K_RIGHT:
                player_rect.move_ip(10, 0)
            elif event.key == pygame.K_UP:
                player_rect.move_ip(0, -10)
            elif event.key == pygame.K_DOWN:
                player_rect.move_ip(0, 10)
            elif event.key == pygame.K_SPACE:
                current_time = pygame.time.get_ticks()  # get the current time
                if current_time - last_shot_time > 500:  # only shoot if at least 500ms has passed since the last shot
                    bullet_rect.center = player_rect.center
                    bullet_heading = math.atan2(pygame.mouse.get_pos()[1] - player_rect.centery,
                                                pygame.mouse.get_pos()[0] - player_rect.centerx)
                    last_shot_time = current_time  # update the last shot time

    # Move the bullet
    bullet_rect.move_ip(bullet_speed * math.cos(bullet_heading), bullet_speed * math.sin(bullet_heading))

    # Draw the scene
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(bullet_image, bullet_rect)

    # Update the display
    pygame.display.flip()
