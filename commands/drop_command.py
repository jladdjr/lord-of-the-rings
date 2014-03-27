#!/usr/bin/python

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
        itemToRemove = raw_input("\nWhich item do you want to drop? \n")
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        item = inventory.getItemByName(itemToRemove)

        #Checks if item is in inventory
        print ""
        if not item:
            print "%s is not in your inventory!" %itemToRemove
            return

        print "Dropping %s" %itemToRemove
        print "Unequipping %s" %itemToRemove
        
        inventory.removeItem(item)
        
        #If item is currently equipped
        if equipped.containsItem(item):
            equipped.removeItem(item)
        
        #Adds item to space
        location = self._player.getLocation()
        location.addItem(item)
