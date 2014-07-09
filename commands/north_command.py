#!/usr/bin/python

from command import Command

class NorthCommand(Command):
    """
    North command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes north command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, time = True)

        self._player = player

    def execute(self):
        """
        Run North command.
        """
        #Make sure that exit exists
        if not self._player.canMoveNorth():
            print "Cannot move North."
            return

        #User graphic
        print "--------------------------------"
        print "         Moving North"
        print "              /\                "
        print "              ||                "
        print "              ||                "
        print ""
        
        #Actual move execution and user output
        self._player.moveNorth()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description