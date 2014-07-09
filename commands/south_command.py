#!/usr/bin/python

from command import Command

class SouthCommand(Command):
    """
    South command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes south command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation, time = True)

        self._player = player

    def execute(self):
        """
        Run South command.
        """
        #Make sure that exit exists
        if not self._player.canMoveSouth():
            print "Cannot move South."
            return

        #User graphic
        print "--------------------------------"
        print "         Moving South"
        print "              ||                "
        print "              ||                "
        print "              \/                "
        print ""
        
        #Actual move execution and user output
        self._player.moveSouth()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description