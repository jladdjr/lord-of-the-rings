from command import Command

class DropCommand(Command):
    """
    Allows player to drop an item from inventory into room.
    """

    def __init__(self, name, explanation, player, #space#):
        """
        Initializes new drop command.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Create local copies of player and space
        player = self._player
        player = self._board

    def execute(self, self_player, #space#):
        """
        Run Drop command.
        """

        item_to_remove = raw_input("Which item do you want to drop?" )
        if item in self._player.inventory:
            self._player.inventory.remove(item)
        else:
            print "Item does not exist in inventory."
        
        
