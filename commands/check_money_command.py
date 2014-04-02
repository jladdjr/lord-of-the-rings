#!/usr/bin/python

from command import Command

class CheckMoneyCommand(Command):
    """
    Prints player money.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check stats command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Prints player money.
        """
        money = self._player.getMoney()
        name = self._player.getName()

        print "%s currently has %s total money!" %(name, money)
                
