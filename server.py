import socket
from _thread import *
import pickle
from ServerData import *
from game import Game

server = "192.168.1.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            
            if gameId in games:
                print("got here")
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        #game.resetWent()
                        pass
                    elif data != "get":
                        #game.play(p, data)
                        pass

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

def main():

    idCount = 0

    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)

        idCount += 1
        p = 0
        gameId = (idCount - 1)//3
        if idCount % 3 == 1:
            games[gameId] = Game(gameId)
            print("GAME ID", gameId)
            print("Creating a new game...")
        else:
            games[gameId].ready = True
            p = idCount - 1

        start_new_thread(threaded_client, (conn, p, gameId))

if __name__ == "__main__":
    main()
