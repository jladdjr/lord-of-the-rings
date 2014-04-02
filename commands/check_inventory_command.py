#!/usr/bin/python

from command import Command
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
        playerName = self._player.getName()
        inventory = self._player.getInventory()
        inventoryList = inventory.getItems()

        totalWeight = 0
        
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
            
            print "\t%s: %s" %(itemName, itemDescription)
            print "\t%s weights %s." %(itemName, itemWeight)

            if isinstance(item, Armor):
                print "\t%s has a defense of %s." %(itemName, itemDefense)
            elif isinstance(item, Weapon):
                print "\t%s has an attack value of %s." %(itemName, itemAttack)
            elif isinstance(item, Potion):
                print "\t%s has a healing value of %s." %(itemName, itemHeal)
            print ""

            totalWeight += int(itemWeight)

        print "\tTotal weight of inventory: %s" %totalWeight
