import socket
import pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.server = "192.168.1.2"
        self.server = "10.0.0.99"
        self.port = 54555
        self.addr = (self.server, self.port)
        #self.p = self.connect()

    def getP(self, data):
        self.client.send(str.encode(data))
        return self.client.recv(2048).decode()

    def connect(self):
        try:
            self.client.connect(self.addr)
            #return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as e:
            print(e)

