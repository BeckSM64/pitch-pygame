import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.99"
        self.port = 54555
        self.addr = (self.server, self.port)
        self.p = None

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass

    def getPlayer(self, data):
        try:
            self.client.send(str.encode(data))
            return int(self.client.recv(2048).decode())
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*4))
        except socket.error as e:
            print(e)

