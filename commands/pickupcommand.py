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

        #Create local copies of player, inventory, and location
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
            
