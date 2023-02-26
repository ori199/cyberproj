import pygame

pygame.init()
screenh = 500
screenw = 500


#fff

win = pygame.display.set_mode((screenw,screenh))
pygame.display.set_caption("first game")
p1x = 50
p1y = 50
p2x = 150
p2y = 50

width = 40
height = 60
vel = 5

run = True
radios = 20
colorblue=(0,191,255)
bullet_img = pygame.image.load("bullet.png")
bulletx = 0
bullety = 0


def bulletshot(x,y,way):
    if way == 'right':
        x += vel
    elif way == 'left':
        x -= vel
    elif way == 'down':
        y += vel
    elif way == 'up':
        y -= vel
    win.blit(bullet_img , (30, 30))
    pygame.display.flip()


def player(x,y):
    pygame.draw.circle(win,colorblue,(x+radios,y+radios),radios,int(radios/4))
    pygame.draw.line(win,colorblue,(x+radios-int(radios/10),y+2*radios),(x+radios-int(radios/10),y+6*radios),int(radios/4))
    #hands
    pygame.draw.line(win,colorblue,(x+radios-int(radios/10),y+2*radios),((x+radios-int(radios/10))-radios,y+4*radios),int(radios/4))
    pygame.draw.line(win, colorblue, (x + radios - int(radios / 10), y + 2 * radios),((x + radios - int(radios / 10)) + radios, y + 4 * radios), int(radios / 4))
    #legs
    pygame.draw.line(win, colorblue, (x + radios - int(radios / 10), y + 6 * radios), ((x + radios - int(radios / 10)) - radios, y + 8 * radios), int(radios / 4))
    pygame.draw.line(win, colorblue, (x + radios - int(radios / 10), y + 6 * radios),((x + radios - int(radios / 10)) + radios, y + 8 * radios), int(radios / 4))
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


def draw_gun(x, y):
    # Draw the gun handle
    pygame.draw.rect(win, gun_color, (x - 20, y + 20, 40, 10))
    pygame.draw.rect(win, gun_color, (x - 15, y + 30, 30, 10))

    # Draw the gun barrel
    barrel_start = (x, y)
    barrel_end = (x, y - 40)
    barrel_width = 10
    pygame.draw.line(win, gun_color, barrel_start, barrel_end, barrel_width)
    pygame.draw.circle(win, gun_color, (x, y - 40), int(barrel_width / 2))

    # Draw the gun sight
    sight_radius = 5
    sight_center = (x, y - 20)
    pygame.draw.circle(win, pygame.Color("red"), sight_center, sight_radius)
    castle(250, 80)
    win.fill((0, 0, 0))
    player(80, 80)
    enemy(180, 80)
    draw_gun(300, 250)
p1shot = False
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

#p1
    if keys[pygame.K_LEFT]:
        p1x -= vel
    if keys[pygame.K_RIGHT]:
        p1x += vel
    if keys[pygame.K_UP]:
        p1y -= vel
    if keys[pygame.K_DOWN]:
        p1y += vel
#p2
    if keys[pygame.K_a]:
        p2x -= vel
    if keys[pygame.K_d]:
        p2x += vel
    if keys[pygame.K_w]:
        p2y -= vel
    if keys[pygame.K_s]:
        p2y += vel
#shoot check

    if keys[pygame.K_SPACE]:
        bulletx = p1x + 2 * radios, p1y
        bullety = p1y + 2 * radios
        bulletshot(bulletx, bullety, 'r')
        p1shot = True
    if p1shot:
        bulletshot(bulletx, bullety, 'r')
    if (int(bulletx)) > (int(screenw)) or ((int(bulletx)) < 0) or int(bullety) > (int(screenh)) or (int(bullety) < 0):
        p1shot = False

    bulletshot(bulletx, bullety, 'r')
    win.fill("black")
    player(p1x, p1y)

    enemy(p2x, p2y)
    pygame.display.update()
    pygame.time.delay(16)
pygame.quit()