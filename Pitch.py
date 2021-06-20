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
from ui.screens.ActiveGamesScreen import *

def main():

    # Default game state
    game_state = GameState.TITLE

    username = None
    gameKey = None
    isHost  = None

    while True:

        # State for title screen
        if game_state == GameState.TITLE:
            game_state, username = TitleScreen().run()

        # State for new game screen
        if game_state == GameState.NEWGAME:
            game_state = GameScreen(username, isHost, gameKey).run()

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
            game_state, isHost, gameKey = HostScreen().run()

        if game_state == GameState.JOIN:
            game_state, isHost, gameKey = JoinScreen().run()

        if game_state == GameState.ACTIVE_GAMES:
            game_state, isHost, gameKey = ActiveGamesScreen().run()

        # State for quitting game
        if game_state == GameState.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
