from command import Command

class DropCommand(Command):
    """
    Allows player to drop an item from inventory into room.
    """

    def __init__(self, name, explanation, player):
        """
        Initializes new pick up command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Drops an item from inventory into room.
        """
        
        itemToRemove = raw_input("Which item do you want to drop? \n")
        inventory = self._player.getInventory()
        item = inventory.getItemByName(itemToRemove)

        #if the item is not recognized, then return without doing anything
        if not item:
            print itemToRemove, " is not in your inventory!"
            return

        print "dropping ", itemToDrop

        #Removes item from inventory
        inventory.removeItem(item)

        #Adds item to current space
        location = self._player.getLocation()
        location.addItem(item)
        
