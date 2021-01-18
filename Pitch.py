from GameState import GameState
from GameScreen import *

def main():

    # Default game state
    game_state = GameState.NEWGAME

    while True:

        # State for title screen
        # if game_state == GameState.TITLE:
        #     game_state = titleScreen()

        # State for new game green
        if game_state == GameState.NEWGAME:
            game_state = gameScreen()

        # State for quitting game
        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == '__main__':
    main()
