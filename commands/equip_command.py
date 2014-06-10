#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.item_set import ItemSet

class EquipCommand(Command):
    """
    Equips player with item in inventory.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new equip command.

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
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        equippable = ItemSet()
        
        #User prompt
        print "%s may equip:" % self._player.getName()
        for item in inventory:
            if (isinstance(item, Weapon) or isinstance(item, Armor)) and \
               item not in equipped:
                print "\t%s" % item.getName()
                equippable.addItem(item)
        print ""

        if equippable.count() == 0:
            print "No equippable items in inventory."
            return
        
        itemToEquip = raw_input("Which item do you want to equip? ")

        #Equip item
        item = inventory.getItemByName(itemToEquip)
        if item:
            self._player.equip(item)
            print "%s equipped %s!" % (self._player.getName(), item.getName())
        else:
            print "Cannot equip %s!" % itemToEquip
