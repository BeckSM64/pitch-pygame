import sys
sys.path.insert(0, '../')
import socket
from _thread import *
import pickle
from ServerData import *
from game import Game

server = "192.168.1.2"
port = 54555

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

def get_card(data):

    # split data to get value and suit
    data = data.split(" ")

    # return the server card
    return SCard(int(data[1]), data[2])

def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096 * 2).decode()
            
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        #game.resetWent()
                        pass
                    elif "card:" in data:
                        
                        # get card from data
                        s_card = get_card(data)

                        # add card to main pile
                        game.mainPile.add_card(s_card)

                        # check if everyone has played a card
                        if len(game.mainPile.cards) == game.numPlayers * 6:

                            # reset deck and shuffle
                            game.deck = SDeck()
                            game.deck.shuffle()

                            # reset main pile
                            game.mainPile = SMainPile()

                            # deal new hands
                            # game.p1Hand = game.dealHand()
                            # game.p2Hand = game.dealHand()
                            # game.p3Hand = game.dealHand()
                            game.dealHands()

                    # send updated game back to all players
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
        gameId = (idCount - 1)//4
        if idCount % 4 == 1:
            games[gameId] = Game(gameId)
            print("GAME ID", gameId)
            print("Creating a new game...")
        else:
            # TODO: Make this work for three or more players, not just two
            games[gameId].ready = True
            p = idCount - 1

        # Add player to player list
        games[gameId].newPlayer(p)

        # Increment number of players in game
        games[gameId].numPlayers += 1

        start_new_thread(threaded_client, (conn, p, gameId))

if __name__ == "__main__":
    main()
