#!/usr/bin/python

from command import Command
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.charm import Charm
from items.item import Item

class CheckInventoryCommand(Command):
    """
    Displays player inventory and details item stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check inventory command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Displays character inventory.
        """
        #Get basic player information
        playerName = self._player.getName()
        inventory = self._player.getInventory()
        inventoryList = inventory.getItems()

        #Cycle through player's inventory, obtaining item stats
        print "%s's inventory:\n" % playerName
        for item in inventoryList:
            itemName = item.getName()
            itemDescription = item.getDescription()
            itemWeight = str(item.getWeight())
            itemCost = str(item.getCost())
            
            if isinstance(item, Armor):
                itemDefense = str(item.getDefense())
            elif isinstance(item, Weapon):
                itemAttack = str(item.getAttack())
            elif isinstance(item, Potion):
                itemHeal = str(item.getHealing())
            elif isinstance(item, Charm):
                itemDefense = str(item.getDefense())
                itemAttack = str(item.getAttack())
                itemHp = str(item.getHp())
            elif isinstance(item, Item):
                pass
            else:
                errorMsg = "CheckInventoryCommand given invalid item type."
                raise AssertionError(errorMsg)

            #Print stats of given item in inventory
            print "\t%s: %s." % (itemName, itemDescription)

            if isinstance(item, Armor):
                print "\t%s has a defense of %s." % (itemName, itemDefense)
            elif isinstance(item, Weapon):
                print "\t%s has an attack value of %s." % (itemName, 
                    itemAttack)
            elif isinstance(item, Potion):
                print "\t%s has a healing value of %s." % (itemName, itemHeal)
            elif isinstance(item, Charm):
                print ("\t%s has an attack bonus of %s, a defense bonus of %s," 
                    " and a HP bonus of %s." % (itemName, itemAttack, 
                    itemDefense, itemHp))
            elif isinstance(item, Item):
                pass
            else:
                errorMsg = "CheckInventoryCommand given invalid item type."
                raise AssertionError(errorMsg)
            
            print "\t%s weighs %s and costs %s." % (itemName, itemWeight, 
                itemCost)
            print ""

        print "\tTotal weight of inventory: %s." % inventory.getWeight()