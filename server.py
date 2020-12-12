import socket
from _thread import *
import pickle
from ServerData import *

server = "192.168.1.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

# Setup game objects
deck = SDeck()
deck.shuffle()

def threaded_client(conn, p):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if data == "get hand":
                print("Got request for card")
                test_hand = deck.deal_hand()
                conn.send(pickle.dumps(test_hand))
        except:
            break

    print("Lost connection")
    idCount -= 1
    conn.close()

def main():

    idCount = 0

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        idCount += 1
        p = 0
        if idCount % 4 == 1:
            print("Creating a new game...")
        else:
            p = idCount - 1

        start_new_thread(threaded_client, (conn, p))

if __name__ == "__main__":
    main()
