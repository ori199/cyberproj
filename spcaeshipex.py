import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Ship")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the initial position of the space ship
spaceship_x = 400
spaceship_y = 500

# Set the movement speed of the space ship
spaceship_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the space ship based on the user's input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed
    if keys[pygame.K_UP]:
        spaceship_y -= spaceship_speed
    if keys[pygame.K_DOWN]:
        spaceship_y += spaceship_speed

    # Draw the space ship on the screen
    screen.fill(BLACK)
    pygame.draw.polygon(screen, WHITE, [(spaceship_x, spaceship_y),
                                        (spaceship_x + 30, spaceship_y),
                                        (spaceship_x + 45, spaceship_y + 30),
                                        (spaceship_x + 30, spaceship_y + 45),
                                        (spaceship_x, spaceship_y + 45),
                                        (spaceship_x - 15, spaceship_y + 30)])

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
