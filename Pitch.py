import sys
from game.logic.GameState import GameState
from ui.screens.GameScreen import *
from ui.screens.TitleScreen import *
from ui.screens.DisconnectScreen import *
from ui.screens.ServerErrorScreen import *
from ui.screens.OptionsScreen import *
from ui.screens.VideoSettingsScreen import *
from ui.screens.HostScreen import *
from ui.screens.JoinScreen import *

def main():

    # Default game state
    game_state = GameState.TITLE

    username   = None
    gameKey    = None
    gameName   = None
    isHost     = None
    maxPlayers = None
    gameMode   = None

    while True:

        # State for title screen
        if game_state == GameState.TITLE:
            game_state, username = TitleScreen().run()

        # State for new game screen
        if game_state == GameState.NEWGAME:
            game_state = GameScreen(username, isHost, gameName, gameKey, maxPlayers, gameMode).run()

        # State for disconnect screen
        if game_state == GameState.DISCONNECT:
            game_state = DisconnectScreen().run()

        # State for server connection error screen
        if game_state == GameState.SERVER_ERROR:
            game_state = ServerErrorScreen().run()

        # State for options screen
        if game_state == GameState.OPTIONS:
            game_state = OptionsScreen().run()

        # State for video settings screen
        if game_state == GameState.VIDEO_SETTINGS:
            game_state = VideoSettingsScreen().run()

        if game_state == GameState.HOST:
            game_state, isHost, gameName, gameKey, maxPlayers, gameMode = HostScreen().run()

        if game_state == GameState.JOIN:
            game_state, isHost, gameName, gameKey = JoinScreen().run()

        # State for quitting game
        if game_state == GameState.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
