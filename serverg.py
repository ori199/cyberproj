import socket
import pygame
p1x = 50
p1y = 50
p2x = 150
p2y = 50
width = 40
height = 60
vel = 10
run = True
radios = 20
screenh = 1080
screenw = 1920
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


bullets = []
players = []


# Draw surf at the new coordinates
listofcollisions = []





def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(3)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()