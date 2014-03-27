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
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Run East command.
        """
        print "--------------------------------"
        print "         moving east"
        print "      ----------------->        "
        print ""
        print "--------------------------------"

        #Move East
        self._player.moveEast()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to ", name 
        print description 
