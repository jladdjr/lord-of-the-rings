#!/usr/bin/python

from command import Command

class Location(Command):
    """
    Allows player to drop an item from inventory into room.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new pick up command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Drops an item from inventory into room.
        """
        choice = input("Where do you want to go?")
        player._location = choice
        try:
            choice = input("Where do you want to go?")
            player._location = choice
        except:
            print "failed"

            
        
