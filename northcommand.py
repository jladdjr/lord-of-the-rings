from command import Command
import space_dictionary
import game_stats

class NorthCommand(Command):
    """
    North command.
    """

    def __init__(self, name, explanation):
        """
        Initializes new north command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

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
        #what is the current space?
        self.current_space = game_stats.current_space
        #what is north of the current space?
        north_space = space_dictionary.dictionary[self.current_space]['north']
        
        print "Welcome to ",north_space
        game_stats.current_space = north_space
        
