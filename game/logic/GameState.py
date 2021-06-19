from enum import Enum

class GameState(Enum):
    QUIT           = -1
    TITLE          = 0
    NEWGAME        = 1
    DISCONNECT     = 2
    SERVER_ERROR   = 3
    OPTIONS        = 4
    VIDEO_SETTINGS = 5
    HOST           = 6
