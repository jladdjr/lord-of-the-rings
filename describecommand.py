from command import Command
import space_dictionary
import game_stats

class DescribeCommand(Command):
    """
    Describe the current space.
    """

    def __init__(self, name, explanation):
        """
        Initializes new describe command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run Describe command.
        """
        #current space
        self.current_space=game_stats.current_space
        print "You are currently in %s" %(self.current_space)
        print ""
        
        #prints the current description of the room
        print space.current_space.description
