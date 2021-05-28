import pygame
from pygame.locals import *
from Button import Button

class BidScreen:
    def __init__(self):

        # Screen width and height
        self.w, self.h = pygame.display.get_surface().get_size()

        # Initialize buttons for bid screen
        self.BUTTON_WIDTH  = 100
        self.BUTTON_HEIGHT = 100
        self.BUTTON_PADDING = 5
        self.COLOR         = (255, 255, 255)
        self.TEXT_COLOR    = (0, 0, 0)

        # Lists of different bid buttons. Different button lists will be used depending
        # on which bid options are valid at the time each player makes their bid
        self.buttonList1    = self.setButtonList1()
        self.buttonList2    = self.setButtonList2()
        self.buttonList3    = self.setButtonList3()
        self.buttonList4    = self.setButtonList4()
        self.buttonListPass = self.setButtonListPass()
        self.buttonList     = self.buttonList4

    def draw(self, screen, game):

        # Get the current highest bid
        highestBid = game.getHighestBid()

        # Determine which bid options should be displayed
        if highestBid == 0:

            # If the player is stuck with it, force them to bid 2
            if (((len(game.players)) - 1) == (game.getNumberOfBids())):
                self.buttonList = self.buttonList1
            else:
                self.buttonList = self.buttonList4

        # If bid is 2, bid options are 3, 4, and pass
        elif highestBid == 2:
            self.buttonList = self.buttonList3

        # If bid is 3, bid options are 4 and pass
        elif highestBid == 3:
            self.buttonList = self.buttonList2

        # If bid is 4, bid options are just pass
        elif highestBid == 4:
            self.buttonList = self.buttonListPass

        # Draw the bid buttons to the screen
        for button in self.buttonList:
            button.draw(screen)

    def setButtonList4(self):
        bidButton2    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT, 
                            (self.w / 2) - (self.BUTTON_WIDTH * 2) - (self.BUTTON_PADDING * 3),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2), self.COLOR, self.TEXT_COLOR, "2"
                        )
        bidButton3    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH) - (self.BUTTON_PADDING),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "3"
                        )
        bidButton4    = Button(self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) + (self.BUTTON_PADDING),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "4"
                        )
        bidButtonPass = Button(self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) + (self.BUTTON_WIDTH) + (self.BUTTON_PADDING * 3),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR,
                            self.TEXT_COLOR,
                            "PASS"
                        )

        buttonList = [bidButton2, bidButton3, bidButton4, bidButtonPass]
        return buttonList

    def setButtonList3(self):
        bidButton3    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH / 2) - (self.BUTTON_WIDTH) - (self.BUTTON_PADDING),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR,
                            self.TEXT_COLOR,
                            "3"
                        )
        bidButton4    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH / 2),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "4"
                        )
        bidButtonPass = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH / 2) + (self.BUTTON_WIDTH) + (self.BUTTON_PADDING),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "PASS"
                        )

        buttonList = [bidButton3, bidButton4, bidButtonPass]
        return buttonList

    def setButtonList2(self):
        bidButton4    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH) - (self.BUTTON_PADDING),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "4"
                        )
        bidButtonPass = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2), 
                            self.COLOR,
                            self.TEXT_COLOR,
                            "PASS"
                        )

        buttonList = [bidButton4, bidButtonPass]
        return buttonList

    def setButtonList1(self):
        bidButton2    = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH / 2),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR, self.TEXT_COLOR,
                            "2"
                        )

        buttonList = [bidButton2]
        return buttonList

    def setButtonListPass(self):
        bidButtonPass = Button(
                            self.BUTTON_WIDTH,
                            self.BUTTON_HEIGHT,
                            (self.w / 2) - (self.BUTTON_WIDTH / 2),
                            (self.h / 2) - (self.BUTTON_HEIGHT / 2),
                            self.COLOR,
                            self.TEXT_COLOR,
                            "PASS"
                        )

        buttonList = [bidButtonPass]
        return buttonList
