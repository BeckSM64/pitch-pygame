import sys
sys.path.insert(0, '../')
import socket
from _thread import *
import pickle
from ServerData import *
from Game import Game

#server = "192.168.1.2"
server = "10.0.0.99"
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

def get_bid(data):

    # Bid value located at position 1
    data = data.split(" ")
    bid = data[1]

    # Convert string bid to int
    if bid == "PASS":
        bid = 0
    else:
        bid = int(bid)

    return bid

def threaded_client(conn, addr):
    global idCount
    p, gameId = joinGame(conn, addr)
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

                        for playerCard in game.players[p].playerHand.cards:
                            if playerCard.value == s_card.value and playerCard.suit == s_card.suit:
                                game.players[p].playerHand.cards.remove(playerCard)

                        # add card to main pile
                        game.mainPile.add_card(s_card)

                        # update trump
                        if game.mainPile.size() == 1 and game.trump is None:
                            game.trump = s_card.suit

                        if game.mainPile.isBestCard(s_card, game.trump):
                            game.winningTrick = game.players[p].id

                        # update current suit
                        if game.mainPile.size() == 1 and game.currentSuit == None:
                            game.currentSuit = s_card.suit

                        # update player turn
                        # TODO: This may need to change after trick mechanics are implemented
                        game.determinePlayerTurn()
                    
                    elif "ready" == data:

                        # Award cards from trick to winning player
                        for player in game.players:
                            if player.id == game.winningTrick:
                                player.wonCards.cards.extend(game.mainPile.cards)

                        # Reset main pile
                        game.mainPile = SMainPile()

                        # Make winner of the trick go next
                        if game.winningTrick is not None:
                            for player in game.players:
                                if player.id == game.winningTrick:
                                    player.playerTurn = True
                                else:
                                    player.playerTurn = False

                        game.winningTrick = None
                        game.currentSuit = None

                        # if reached end of round, reset the table
                        if game.isHandsEmpty():

                            # calculate scores
                            game.calculateScores()

                            for player in game.players:

                                player.ready = True
                                player.playerBid = None
                                player.playerBid = None
                                player.playerTurn = False
                                player.roundPoints = 0
                                player.wonCards = SMainPile()
                            
                            game.bidWinner = None
                            game.biddingStage = True

                            # TODO: Fix this
                            game.players[0].playerBidTurn = True

                            # reset trump
                            game.trump = None

                            # reset current suit
                            game.currentSuit = None

                            # reset deck and shuffle
                            game.deck = SDeck()
                            game.deck.shuffle()

                            # reset main pile
                            game.mainPile = SMainPile()

                            # deal new hands
                            game.dealHands()

                            # determine who bids first
                            game.determineFirstBidder()

                    elif "not ready" == data:
                        game.players[p].ready = False

                    elif "bid:" in data:

                        # Get bid from player
                        game.players[p].playerBid = get_bid(data)

                        # Update whose turn it is to bid
                        game.determineBidTurn()

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

def joinGame(conn, addr):
    global idCount
    idCount += 1
    p = 0
    gameId = (idCount - 1)//4
    if idCount % 4 == 1:
        games[gameId] = Game(gameId)
        print("GAME ID", gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = idCount - 1

    # Add player to player list
    games[gameId].newPlayer(p)

    # Increment number of players in game
    games[gameId].numPlayers += 1

    return p, gameId

def main():
    global idCount
    idCount = 0

    while True:
        
        conn, addr = s.accept()
        print("Connected to:", addr)

        start_new_thread(threaded_client, (conn, addr))

if __name__ == "__main__":
    main()
