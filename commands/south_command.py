#!/usr/bin/python

from command import Command

class SouthCommand(Command):
    """
    South command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new south command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Run South command.
        """
        #Make sure there is a south exit
        if not self._player.canMoveSouth():
            print "Cannot move South."
            return

        #Move South
        print "--------------------------------"
        print "         Moving South"
        print "              ||                "
        print "              ||                "
        print "              \/                "
        print ""

        self._player.moveSouth()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to %s." % name 
        print description 
