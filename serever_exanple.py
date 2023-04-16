# import socket programming library
import socket
radios =5
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

# import thread module
from _thread import *
bullets = []
players = []
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
colorblue=(0,191,255)
colorred = (255,0,0)

import threading
players.append(player(50, 50, colorblue,1))
players.append(player(150, 50, colorred,2))
playerpos = [(players[0].x,players[0].y),(players[1].x,players[1].y)]
def update_player_pos(players,index,xpos,y):
    players[index].x = xpos
    players[index].y = xpos

def broadc(clients,message):
    for c in clients:
        c.send(message)
def updateplayerposlist(players,playerpos):
    for player in players:
        playerpos[player.number] = (player.x,players.y)
def sendpostoclients(players)
# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')


            break

        # reverse the given string from client
        data = data[::-1]

        # send back reversed string to client
        c.send(data)

    # connection closed
    c.close()


def Main():
    host = ""

    # reserve a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    clients =[]
    # a forever loop until client wants to exit
    while True:
        # establish connection with client
        c, addr = s.accept()
        clients.append(c)
        # lock acquired by client
        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    Main()