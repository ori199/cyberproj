import pygame
import time
import random

pygame.init()
screenh = 1080
screenw = 1920
BLACK = (0, 0, 0)
white = (255, 255, 255)
win = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("cool game")
p1x = 50
p1y = 50
p2x = 150
p2y = 50
width = 50
height = 50
vel = 10
run = True
radios = 20
colorblue = (0, 191, 255)
spaceshipsize = (50, 50)
bullet_img = pygame.image.load("bullet.png")
bullets = []
players = []
blue_wall = pygame.image.load('wallv3.png').convert()
font = pygame.font.Font(None, 30)
imp = pygame.image.load("C:\\Users\\orira\\PycharmProjects\\pythonProject2\\cyberprojgame\\spaceshipv2.png").convert()
spaceshipup = pygame.transform.scale(imp, spaceshipsize)
spaceshipdown = pygame.transform.rotate(spaceshipup, 180)
spaceshipright = pygame.transform.rotate(spaceshipup, 270)
spaceshipleft = pygame.transform.rotate(spaceshipup, 90)

# Draw surf at the new coordinates
listofcollisions = []


class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, white)

    def render(self, display):
        self.text = self.font.render(str(round(self.clock.get_fps(), 2)), True, white)
        display.blit(self.text, (200, 150))


fps = FPS()


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
for i in range(6):
    new_wall1 = Wall(random.randrange(0, screenw-300), random.randrange(0, screenh-50), wall_blue_left)
    new_wall2 = Wall(random.randrange(0, screenw - 300), random.randrange(0, screenh - 50), blue_wall)
    wall_group.add(new_wall1)
    wall_group.add(new_wall2)



# Using blit to copy content from one surface to other
def drawspcaship(x, y, facing):
    pos = (x, y)
    if facing == 'up':
        win.blit(spaceshipup, pos)
        #pygame.display.flip()
    elif facing == 'down':
        win.blit(spaceshipdown, pos)
        #pygame.display.flip()
    elif facing == 'right':
        win.blit(spaceshipright, pos)
        #pygame.display.flip()
    else:
        win.blit(spaceshipleft, pos)
        #pygame.display.flip()


class projectile(object):
    def __init__(self, x, y, radius, color, facing, shooter):
        self.vel = vel * 1.5
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.shooter = shooter
        self.hit = False

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius, )


class player(object):
    def __init__(self, x, y, color, number):
        self.facing = 'right'
        self.color = color
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.vel = 5
        self.hp = 5
        self.alive = True
        self.number = number
        self.lastshottime = time.time()


def bulletdraw(bullet):
    pygame.draw.rect(win, colorred,
                     [bullet.x, bullet.y, 2, 4], 2)
    #pygame.display.flip()


def drawwalls():
    pygame.draw.rect(win, (0, 0, 255),
                     [20, 20, 80, 40], 2)


def playerdraw(x, y, color):
    pygame.draw.circle(win, color, (x + radios, y + radios), radios, int(radios / 4))
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 2 * radios),
                     (x + radios - int(radios / 10), y + 6 * radios), int(radios / 4))
    # hands
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 2 * radios),
                     ((x + radios - int(radios / 10)) - radios, y + 4 * radios), int(radios / 4))
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 2 * radios),
                     ((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    # legs
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 6 * radios),
                     ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 6 * radios),
                     ((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))


colorred = (255, 0, 0)


def enemy(x, y):
    pygame.draw.circle(win, colorred, (x + radios, y + radios), radios, int(radios / 4))
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 2 * radios),
                     (x + radios - int(radios / 10), y + 6 * radios), int(radios / 4))
    # hands
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 2 * radios),
                     ((x + radios - int(radios / 10)) - radios, y + 4 * radios), int(radios / 4))
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 2 * radios),
                     ((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    # legs
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 6 * radios),
                     ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 6 * radios),
                     ((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))


def castle(x, y):
    pygame.draw.rect(win, (0, 0, 255),
                     [x, y, radios * 4, radios * 5], 2)


gun_color = pygame.Color("gray")

players.append(player(50, 50, colorblue, 1))
players.append(player(150, 50, colorred, 2))
clock = pygame.time.Clock()
# main game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    keysre = pygame.key.get_repeat()
    # p1 controls
    if keys[pygame.K_LEFT] and players[0].x > 0:
        players[0].x -= vel
        players[0].facing = 'left'

    if keys[pygame.K_RIGHT] and players[0].x + players[0].width < screenw:
        players[0].x += vel
        players[0].facing = 'right'
    if keys[pygame.K_UP] and players[0].y > 0:
        players[0].y -= vel
        players[0].facing = 'up'
    if keys[pygame.K_DOWN] and players[0].y + players[0].height < screenh:
        players[0].y += vel
        players[0].facing = 'down'
    # p2 controls
    if keys[pygame.K_a] and players[1].x > 0:
        players[1].x -= vel
        players[1].facing = 'left'
    if keys[pygame.K_d] and players[1].x + players[0].width < screenw:
        players[1].x += vel
        players[1].facing = 'right'
    if keys[pygame.K_w] and players[1].y > 0:
        players[1].y -= vel
        players[1].facing = 'up'
    if keys[pygame.K_s] and players[1].y + players[0].height < screenh:
        players[1].y += vel
        players[1].facing = 'down'
    # shoot check
    # checking if bullets are on the screen borders
    # updating bullet positions
    for bullet in bullets:
        if bullet.x < screenw and bullet.x > 0 and bullet.y < screenh and bullet.y > 0:
            if bullet.facing == 'right':
                bullet.x += bullet.vel
            if bullet.facing == 'left':
                bullet.x -= bullet.vel
            if bullet.facing == 'up':
                bullet.y -= bullet.vel
            if bullet.facing == 'down':
                bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    # Creating bullets adding to the bullets list with direction
    win.fill(BLACK)

    if keys[pygame.K_KP0] and players[0].alive and (time.time() - players[0].lastshottime) >= 1:
            # if len(bullets) < 20:
            # clock.tick(30)
            if players[0].facing == 'right':
                bullets.append(projectile(round(players[0].x + players[0].width),
                                          round(players[0].y + players[0].height // 2), 6, (255, 0, 0),
                                          players[0].facing, players[0]))
                players[0].lastshottime = time.time()
            elif players[0].facing == 'left':
                bullets.append(
                    projectile(round(players[0].x - players[0].width // 2),
                               round(players[0].y + players[0].height // 2), 6, (255, 0, 0), players[0].facing, players[0]))
                players[0].lastshottime = time.time()
            elif players[0].facing == 'up':
                bullets.append(projectile(round(players[0].x + players[0].width // 2),
                                          round(players[0].y), 6, (255, 0, 0),
                                          players[0].facing, players[0]))
                players[0].lastshottime = time.time()

            else:
                bullets.append(
                    projectile(round(players[0].x + players[0].width // 2),
                               round(players[0].y + players[0].height), 6, (255, 0, 0), players[0].facing, players[0]))
                players[0].lastshottime = time.time()
    if keys[pygame.K_SPACE] and players[1].alive and (time.time() - players[1].lastshottime) >= 1:
            # if len(bullets) < 20:
            # clock.tick(30)
            if players[1].facing == 'right':
                bullets.append(projectile(round(players[1].x + players[1].width),
                                          round(players[1].y + players[1].height // 2), 6, (255, 0, 0),
                                          players[1].facing, players[1]))
                players[1].lastshottime = time.time()
            elif players[1].facing == 'left':
                bullets.append(
                    projectile(round(players[1].x - players[1].width // 2),
                               round(players[1].y + players[1].height // 2), 6, (255, 0, 0), players[1].facing, players[1]))
                players[1].lastshottime = time.time()
            elif players[1].facing == 'up':
                bullets.append(projectile(round(players[1].x + players[1].width // 2),
                                          round(players[1].y), 6, (255, 0, 0),
                                          players[1].facing, players[0]))
                players[1].lastshottime = time.time()

            else:
                bullets.append(
                    projectile(round(players[1].x + players[1].width // 2),
                               round(players[1].y + players[1].height), 6, (255, 0, 0), players[1].facing, players[1]))
                players[1].lastshottime = time.time()
                # win.blit(mazeimg, surf_center)
    # pygame.display.flip()
    # Check if the gun hit an enemy
    for player in players:
        for bullet in bullets:
            if (int(player.x) <= int(bullet.x) <= int(player.x + player.width)) and (
                    int(player.y) <= int(bullet.y) <= int(player.y + player.height)) and (
                    bullet.shooter != player) and player.alive and (not bullet.hit):
                player.hp -= 1
                bullet.hit = True
                if player.hp == 0:
                    player.alive = False
                    bullets.remove(bullet)
                break
    for bullet in bullets:
        if not bullet.hit:
            bulletdraw(bullet)

    for player in players:
        if player.alive:
            drawspcaship(player.x, player.y, player.facing)
            # playerdraw(player.x, player.y, player.color)
        #else: players.remove(player)
    # Draw the score
    wall_group.draw(win)
    for player in players:
        hp_text = font.render("player" + str(player.number) + ": " + str(player.hp), True, (255, 255, 255))
        win.blit(hp_text, (player.number * 200, 10))
    fps.render(win)
    fps.clock.tick(60)
    pygame.display.update()
    # clock.tick(60)
pygame.quit()
