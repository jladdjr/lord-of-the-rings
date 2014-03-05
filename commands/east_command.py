from command import Command
import space_dictionary
from player import Player
import space

class EastCommand(Command):
    """
    East command.
    """

    def __init__(self, name, explanation):
        """
        Initializes new north command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run East command.
        """
        print "--------------------------------"
        print "         moving east"
        print "      ----------------->        "
        print ""
        #what is the current space?
        self.current_space = Player.current_space
        #what is north of the current space?
        east_space = space_dictionary.dictionary[self.current_space]['east']
        
        print "Welcome to ",east_space
        Player.current_space = east_space
        self.current_space=east_space
        print space.current_space.description
 
