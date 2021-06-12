from game.logic.GameState import GameState
from ui.screens.GameScreen import *
from ui.screens.TitleScreen import *
from ui.screens.DisconnectScreen import *
from ui.screens.ServerErrorScreen import *
from ui.screens.OptionsScreen import *
from ui.screens.VideoSettingsScreen import *

def main():

    # Default game state
    game_state = GameState.TITLE

    while True:

        # State for title screen
        if game_state == GameState.TITLE:
            game_state, username = TitleScreen().run()

        # State for new game screen
        if game_state == GameState.NEWGAME:
            game_state = gameScreen(username)

        # State for disconnect screen
        if game_state == GameState.DISCONNECT:
            game_state = disconnectScreen()

        # State for server connection error screen
        if game_state == GameState.SERVER_ERROR:
            game_state = ServerErrorScreen().run()

        # State for options screen
        if game_state == GameState.OPTIONS:
            game_state = optionsScreen()

        # State for video settings screen
        if game_state == GameState.VIDEO_SETTINGS:
            game_state = videoSettingsScreen()

        # State for quitting game
        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == '__main__':
    main()
