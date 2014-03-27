from command import Command

class NorthCommand(Command):
    """
    North command.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new north command.

        @param name:            Command's name.
        @param explanation:     Description of what command does.
        @param player:          Reference to command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Run North command.
        """
        print "--------------------------------"
        print "         moving north"
        print "              /\                "
        print "              ||                "
        print "              ||                "
        print ""

        #Move North
        self._player.moveNorth()

        space = self._player.getLocation()
        name = space.getName()
        description = space.getDescription()
        
        print "Welcome to ", name 
        print description 
