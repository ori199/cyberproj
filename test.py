import pygame
import socket
import pickle

# initialize pygame
pygame.init()

# set up the screen
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Game")

# set up the clock
clock = pygame.time.Clock()

# set up the network
HOST = 'localhost'
PORT = 8888
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)
print("Waiting for connection...")

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# define game objects
class Stickman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 100
        self.color = WHITE
        self.speed = 5

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Projectile:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = RED
        self.speed = 10
        self.direction = direction

    def move(self):
        if self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

# create the stickmen
stickman1 = Stickman(100, 100)
stickman2 = Stickman(400, 100)

# create a list for the projectiles
projectiles = []

# define a function for sending and receiving data over the network
def send_data(data):
    conn1.send(pickle.dumps(data))
    conn2.send(pickle.dumps(data))

def receive_data():
    data1 = pickle.loads(conn1.recv(1024))
    data2 = pickle.loads(conn2.recv(1024))
    return data1, data2

# set up the game loop
running = True
while running:
    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                stickman1.move_left()
                send_data(("move", "left"))
            elif event.key == pygame.K_RIGHT:
                stickman1.move_right()
                send_data(("move", "right"))
            elif event.key == pygame.K_SPACE:
                projectiles.append(Projectile(stickman1.x + stickman1.width/2, stickman1.y + stickman1.height/2, "right"))
                send_data(("shoot", "right"))

    # move and draw the stickmen
    screen.fill(BLACK)
    stickman1
