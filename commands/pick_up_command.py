from command import Command

class PickUpCommand(Command):
    """
    Allows a player to pick up an item from a location.
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
        Picks up an item from a room and adds it to inventory.
        """
        itemToAdd = raw_input("Which item do you want to pick up? ")
        location = self._player.getLocation()
        items = location.getItemSet()
        item = items.getItemByName(itemToAdd)
        
        if not item:
            print "Space does not contain item."
            return

        #Adds item to inventory
        inventory = self._player.getInventory()
        inventory.addItem(item)

        #Removes item from space
        location.removeItem(item)
