from command import Command
from space import Space
from player import Player

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
        current_space=Player.current_space
        print "You are currently in %s" %(self.current_space)
        print ""
        
        #prints the current description of the room
        print Space.current_space.description

