#!/usr/bin/python

from command import Command
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion

class CheckInventoryCommand(Command):
    """
    Prints player inventory and details item stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check inventory command.

        @param name: Command name.
        @param explanation: Explanation of command.
        @param player: The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Displays character inventory.
        """
        #Get basic player information
        playerName = self._player.getName()
        inventory = self._player.getInventory()
        inventoryList = inventory.getItems()

        totalWeight = 0

        #Sort inventory
        sortedInventory = []
        for item in inventoryList:
            if isinstance(item, Weapon):
                sortedInventory.append(item)
        for item in inventoryList:
            if isinstance(item, Armor):
                sortedInventory.append(item)
        for item in inventoryList:
            if isinstance(item, Potion):
                sortedInventory.append(item)
        for item in inventoryList:
            if item not in sortedInventory:
                sortedInventory.append(item)
            
        inventoryList = sortedInventory

        #Cycle through player's inventory, obtaining item stats
        print "%s's inventory:\n" %playerName
        for item in inventoryList:
            itemName = item.getName()
            itemDescription = item.getDescription()
            itemWeight = str(item.getWeight())

            if isinstance(item, Armor):
                itemDefense = str(item.getDefense())
            elif isinstance(item, Weapon):
                itemAttack = str(item.getAttack())
            elif isinstance(item, Potion):
                itemHeal = str(item.getHealing())

            #Print item stats of given item in inventory
            print "\t%s: %s." %(itemName, itemDescription)

            if isinstance(item, Armor):
                print "\t%s has a defense of %s." %(itemName, itemDefense)
            elif isinstance(item, Weapon):
                print "\t%s has an attack value of %s." %(itemName, itemAttack)
            elif isinstance(item, Potion):
                print "\t%s has a healing value of %s." %(itemName, itemHeal)
            print "\t%s weights %s." %(itemName, itemWeight)
            print ""

            totalWeight += int(itemWeight)

        print "\tTotal weight of inventory: %s." %totalWeight
