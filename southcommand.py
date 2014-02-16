from command import Command
import space_dictionary
import game_stats

class SouthCommand(Command):
    """
    South command.
    """

    def __init__(self, name, explanation):
        """
        Initializes new north command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run South command.
        """
        print "--------------------------------"
        print "         moving south"
        print "              ||                "
        print "              ||                "
        print "              \/                "
        print ""
        #what is the current space?
        self.current_space = game_stats.current_space
        #what is north of the current space?
        south_space = space_dictionary.dictionary[self.current_space]['south']
        
        print "Welcome to ",south_space
        game_stats.current_space = south_space
        
