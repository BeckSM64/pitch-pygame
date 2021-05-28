import socket
import pickle
import struct

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 54555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)

            # Keep receiving data until whole message is received
            buf = b''
            while len(buf) < 4:
                buf += self.client.recv(4 - len(buf))

            length = struct.unpack('!I', buf)[0]

            data = b''
            while len(data) < length:
                data += self.client.recv(4)

            # Return player id
            return int(data.decode())

        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(str.encode(data))

            # Keep receiving data until whole message is received
            buf = b''
            while len(buf) < 4:
                buf += self.client.recv(4 - len(buf))

            length = struct.unpack('!I', buf)[0]

            data = b''
            while len(data) < length:
                data += self.client.recv(4)
            return pickle.loads(data)

        except socket.error as e:
            print(e)

