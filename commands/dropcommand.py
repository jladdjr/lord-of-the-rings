from command import Command

class DropCommand(Command):
    """
    Allows player to drop an item from inventory into room.
    """

    def __init__(self, name, explanation, player):
        """
        Initializes new drop command.
        """
        
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Create local copies of player, inventory, and location
        self._player = player
        self._location = self._player.getLocation()

    def execute(self):
        """
        Drops an item from inventory into room.
        """
        
        item_to_remove = raw_input("Which item do you want to drop?" )
        if self._player.inventory.containsItem(item_to_remove):
            #Removes item from inventory
            self._player.inventory.removeItem(item_to_remove)

            #Adds item to current space
            self._location = self._player.getLocation()
            self._location.addItem(item_to_remove)
            
        else:
            print "Item does not exist in inventory."
        
        
