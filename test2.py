import pygame

pygame.init()
screenh = 1080
screenw = 1920
mazeimg = pygame.image.load("86-860032_maze-clip-art-2d-maze-png.png")

win = pygame.display.set_mode((screenw,screenh))
pygame.display.set_caption("cool game")
p1x = 50
p1y = 50
p2x = 150
p2y = 50
width = 40
height = 60
vel = 10
run = True
radios = 20
colorblue=(0,191,255)
bullet_img = pygame.image.load("bullet.png")
bullets = []
players = []
font = pygame.font.Font(None, 30)
surf_center = (
    (screenw-mazeimg.get_width())/2,
    (screenh-mazeimg.get_height())/2
)

# Draw surf at the new coordinates
listofcollisions = []
class projectile(object):
    def __init__(self,x,y,radius,color,facing,shooter):
        self.vel = vel
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.shooter = shooter
        self.hit = False


    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class player(object):
    def __init__(self,x,y,color,number):
        self.facing = 'right'
        self.color = color
        self.x = x
        self.y = y
        self.width = radios*2
        self.height = radios*8
        self.vel = 5
        self.hp = 5
        self.alive = True
        self.number = number
def bulletdraw(bullet):
        pygame.draw.rect(win, colorred,
                         [bullet.x, bullet.y, 2, 4], 2)
        pygame.display.flip()

def drawwalls ():
    pygame.draw.rect(win, (0, 0, 255),
     [20, 20, 80, 40 ], 2)







def playerdraw(x,y,color):
    pygame.draw.circle(win,color,(x+radios,y+radios),radios,int(radios/4))
    pygame.draw.line(win,color,(x+radios-int(radios/10),y+2*radios),(x+radios-int(radios/10),y+6*radios),int(radios/4))
    #hands
    pygame.draw.line(win,color,(x+radios-int(radios/10),y+2*radios),((x+radios-int(radios/10))-radios,y+4*radios),int(radios/4))
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 2 * radios),((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    #legs
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 6 * radios), ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(win, color, (x + radios - int(radios / 10), y + 6 * radios),((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))
colorred = (255,0,0)
def enemy(x,y):
    pygame.draw.circle(win,colorred,(x+radios,y+radios),radios,int(radios/4))
    pygame.draw.line(win,colorred,(x+radios-int(radios/10),y+2*radios),(x+radios-int(radios/10),y+6*radios),int(radios/4))
    #hands
    pygame.draw.line(win,colorred,(x+radios-int(radios/10),y+2*radios),((x+radios-int(radios/10))-radios,y+4*radios),int(radios/4))
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 2 * radios),((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    #legs
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 6 * radios), ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(win, colorred, (x + radios - int(radios / 10), y + 6 * radios),((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))
def castle(x,y):
    pygame.draw.rect(win, (0, 0, 255),
                     [x, y, radios*4, radios*5], 2)

gun_color = pygame.Color("gray")



players.append(player(50, 50, colorblue,1))
players.append(player(150, 50, colorred,2))
clock = pygame.time.Clock()
# main game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
# p1 controls
    if keys[pygame.K_LEFT] and players[0].x > 0:
        players[0].x -= vel
        players[0].facing = 'left'
    if keys[pygame.K_RIGHT] and players[0].x+players[0].width < screenw:
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
    if keys[pygame.K_d] and players[1].x+players[0].width < screenw:
        players[1].x += vel
        players[1].facing = 'right'
    if keys[pygame.K_w] and players[1].y > 0:
        players[1].y -= vel
        players[1].facing = 'up'
    if keys[pygame.K_s] and players[1].y + players[0].height < screenh:
        players[1].y += vel
        players[1].facing = 'down'
#shoot check

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
    keys2 = pygame.key
# Creating bullets adding to the bullets list with direction

    if keys2[pygame.K_KP0]:
        if len(bullets) < 20:
            if players[0].facing == 'right':
                bullets.append(projectile(round(players[0].x + players[0].width),
                                          round(players[0].y + players[0].height // 2), 6, (255, 0, 0),
                                          players[0].facing, players[0]))
            if players[0].facing == 'left':
                bullets.append(
                    projectile(round(players[0].x - players[0].width // 2),
                               round(players[0].y + players[0].height // 2), 6, (255, 0, 0), players[0].facing, players[0]))
            if players[0].facing == 'up':
                bullets.append(projectile(round(players[0].x + players[0].width // 2),
                                          round(players[0].y), 6, (255, 0, 0),
                                          players[0].facing, players[0]))
            if players[0].facing == 'down':
                bullets.append(
                    projectile(round(players[0].x + players[0].width // 2),
                               round(players[0].y + players[0].height), 6, (255, 0, 0), players[0].facing, players[0]))
    if keys[pygame.K_SPACE]:
        if len(bullets) < 20:
            if players[1].facing == 'right':
                bullets.append(
                    projectile(round(players[1].x + players[1].width),
                               round(players[1].y + players[1].height // 2), 6,
                               (255, 0, 0), players[1].facing,  players[1]))
            if players[1].facing == 'left':
                bullets.append(
                    projectile(round(players[1].x - players[1].width // 2),
                               round(players[1].y + players[1].height // 2), 6,
                               (255, 0, 0), players[1].facing, players[1]))
            if players[1].facing == 'up':
                bullets.append(
                    projectile(round(players[1].x + players[1].width // 2),
                               round(players[1].y ), 6,
                               (255, 0, 0), players[1].facing, players[1]))
            if players[1].facing == 'down':
                bullets.append(
                    projectile(round(players[1].x + players[1].width // 2 ),
                               round(players[1].y + players[1].height), 6,
                               (255, 0, 0), players[1].facing,players[1]))
    win.fill("white")

    #win.blit(mazeimg, surf_center)
    #pygame.display.flip()
    # Check if the gun hit an enemy
    for player in players:
        for bullet in bullets:
            if (int(bullet.x) >= int(player.x) and int(bullet.x) <= int(player.x + player.width)) and (int(bullet.y) >= int(player.y) and int(bullet.y) <= int( player.y + player.height)) and (bullet.shooter != player) and (player.alive) and (not bullet.hit):
                player.hp -= 1
                bullet.hit = True
                if player.hp == 0:
                    player.alive = False
                break
    for bullet in bullets:
        if not bullet.hit:
            bulletdraw(bullet)
    for player in players:
        if player.alive:
            playerdraw(player.x, player.y, player.color)
    # Draw the score
    for player in players:
        hp_text = font.render("player" + str(player.number) + ": " + str(player.hp), True, (255, 255, 255))
        win.blit(hp_text, (player.number*200, 10))
    drawwalls()
    pygame.display.update()
    clock.tick(30)
pygame.quit()