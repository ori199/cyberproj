import socket
import threading
import pickle

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 12345

# bind the socket to a public host and a well-known port
s.bind((host, port))

# listen for incoming connections
s.listen(5)

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        print("New thread started for " + str(addr))

    def run(self):
        print("Connection from : " + str(self.addr))

        # receive data from client
        data_bytes = self.conn.recv(4096)

        # deserialize the object using pickle
        data = pickle.loads(data_bytes)

        # print the received object
        print("Received object:", data)

        # create an object to send
        response = {'name': 'Server', 'message': 'Received object'}

        # serialize the object using pickle
        response_bytes = pickle.dumps(response)

        # send the serialized object over the connection
        self.conn.send(response_bytes)

        # close the connection
        self.conn.close()

while True:
    # wait for a client to connect
    conn, addr = s.accept()

    # start a new thread to handle the client
    new_thread = ClientThread(conn, addr)
    new_thread.start()
