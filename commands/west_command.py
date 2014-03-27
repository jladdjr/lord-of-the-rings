#!/usr/bin/python

from command import Command

class WestCommand(Command):
    """
    West command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new west command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Run West command.
        """
        #Make sure there is a west exit
        if not self._player.canMoveWest():
            print "Cannot move West"
            return

        #Move West
        print "--------------------------------"
        print "         moving west"
        print "      ----------------->        "
        print ""
        print "--------------------------------"

        self._player.moveWest()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to ", name 
        print description 
