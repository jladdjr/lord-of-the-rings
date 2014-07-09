#!/usr/bin/python

from command import Command

class EastCommand(Command):
    """
    East command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes east command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, time = True)

        self._player = player
        
    def execute(self):
        """
        Run east command.
        """
        #Make sure that exit exists
        if not self._player.canMoveEast():
            print "Cannot move East."
            return

        #User graphic
        print "--------------------------------"
        print "         Moving East"
        print "      ----------------->        "
        print ""
        print "--------------------------------"
        
        #Actual move execution and user output
        self._player.moveEast()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description