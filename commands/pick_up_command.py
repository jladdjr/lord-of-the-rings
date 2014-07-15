#!/usr/bin/python

from command import Command

class PickUpCommand(Command):
    """
    Allows a player to pick up an item from its current space.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes pick up command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Picks up an item from a room and adds it to inventory.
        """
        name = self._player.getName()
        location = self._player.getLocation()
        locationItems = location.getItems()

        #User prompt
        print "The following may be picked up by %s:" % name
        for item in locationItems:
            print "\t%s" % item.getName()
        print ""
        
        itemToAdd = raw_input("Which item do you want to pick up? ")
        item = locationItems.getItemByName(itemToAdd)
        
        if not item:
            print "%s does not contain item." % location.getName()
            return

        #Add item to inventory
        self._player.addToInventory(item)
        print ""
        print "Added %s to inventory." % item.getName()

        #Remove item from space
        location.removeItem(item)