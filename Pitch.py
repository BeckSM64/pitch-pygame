from GameState import GameState
from GameScreen import *
from TitleScreen import *
from DisconnectScreen import *

def main():

    # Default game state
    game_state = GameState.TITLE

    while True:

        # State for title screen
        if game_state == GameState.TITLE:
            game_state, username = titleScreen()

        # State for new game screen
        if game_state == GameState.NEWGAME:
            game_state = gameScreen(username)

        # State for disconnect screen
        if game_state == GameState.DISCONNECT:
            game_state = disconnectScreen()

        # State for quitting game
        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == '__main__':
    main()
