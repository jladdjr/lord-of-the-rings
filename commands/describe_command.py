from command import Command
from space import Space
from player import Player

class DescribeCommand(Command):
    """
    Describe the current space.
    """

    def __init__(self, name, explanation, player):
        """
        Initializes new describe command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)
        
        self._player = player

    def execute(self):
        """
        Run Describe command.
        """
        location = self._player.getLocation()
        description = location.getDescription()
        
        print description
