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
        self._location = self._player.getLocation()

    def execute(self):
        """
        Picks up an item from a room and adds it to inventory.
        """

        item_to_add = raw_input("Which item do you want to pick up? ")
        if self._location.containsItem(item_to_add):
            #Adds item to inventory
            self._player.inventory.addItem(item_to_add)

            #Removes item from space
            self._location.removeItem(item_to_add)
            
