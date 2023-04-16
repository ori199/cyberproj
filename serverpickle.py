import socket
import pickle

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# set port number
port = 12345

# connect to the server
s.connect((host, port))

# receive the serialized object
data_bytes = s.recv(4096)

# deserialize the object using pickle
data = pickle.loads(data_bytes)

# print the received object
print(data)

# create an object to send

