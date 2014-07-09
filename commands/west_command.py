#!/usr/bin/python

from command import Command

class WestCommand(Command):
    """
    West command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes west command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, time = True)

        self._player = player

    def execute(self):
        """
        Run west command.
        """
        #Make sure that exit exists
        if not self._player.canMoveWest():
            print "Cannot move west."
            return

        #User graphic
        print "--------------------------------"
        print "         Moving West"
        print "      <-----------------        "
        print ""
        print "--------------------------------"

        #Actual move execution and user output
        self._player.moveWest()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description