from command import Command

class PickUpCommand(Command):
    """
    Allows a player to pick up an item from a location.
    """

    def __init__(self, name, explanation):
        """
        Initializes new pick up command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

    def execute(self):
        """
        Run Pick Up command.
        """
        pass
