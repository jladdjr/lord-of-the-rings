#!/usr/bin/python

from command import Command

class EastCommand(Command):
    """
    East command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new east command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, True)

        self._player = player
        
    def execute(self):
        """
        Run east command.
        """
        #Make sure there is an east exit
        if not self._player.canMoveEast():
            print "Cannot move East."
            return

        #Move East
        print "--------------------------------"
        print "         Moving East"
        print "      ----------------->        "
        print ""
        print "--------------------------------"

        self._player.moveEast()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description 
