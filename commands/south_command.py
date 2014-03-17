from command import Command
import space_dictionary
from player import Player
import space

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
        self.current_space = Player.current_space
        #what is north of the current space?
        south_space = space_dictionary.dictionary[self.current_space]['south']
        
        print "Welcome to ",south_space
        Player.current_space = south_space
        self.current_space=south_space
        print space.current_space.description


