from command import Command
import space_dictionary
from player import Player
import space

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
        self.current_space = Player.current_space
        #what is north of the current space?
        north_space = space_dictionary.dictionary[self.current_space]['north']
        
        print "Welcome to ",north_space
        Player.current_space = north_space
        self.current_space=north_space
        print space.current_space.description
 
