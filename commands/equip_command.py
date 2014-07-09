#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm
from items.item_set import ItemSet

class EquipCommand(Command):
    """
    Equips player with item in inventory.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes equip command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Equips player with item in inventory.
        """
        #Create variables
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        equippable = ItemSet()
        
        #Create list of equippable items
        for item in inventory:
            if (isinstance(item, Weapon) or isinstance(item, Armor) or isinstance(item, Charm)) \
            and item not in equipped:
                equippable.addItem(item)
        
        #If no equippable items
        if equippable.count() == 0:
            print "No equippable items in inventory."
            return

        #User prompt   
        print "%s may equip:" % self._player.getName()
        for item in equippable:
            print "\t%s" % item.getName()
        print ""
        itemToEquip = raw_input("Which item do you want to equip? ")

        #Attempt to equip item
        item = inventory.getItemByName(itemToEquip)
        if item:
            statement = self._player.equip(item)
            print statement
        else:
            print "Item not in inventory."