#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor

class CheckEquipmentCommand(Command):
    """
    Displays player equipment and details equipment stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check equipment command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)
        
        self._player = player

    def execute(self):
        """
        Equips player with item in inventory.
        """
        playerName = self._player.getName()
        equipment = self._player.getEquipped()
        
        #Sorts items
        sortedEquipment = []
        for item in equipment:
            if isinstance(item, Weapon):
                sortedEquipment.append(item)
        for item in equipment:
            if isinstance(item, Armor):
                sortedEquipment.append(item)
        equipment = sortedEquipment

        #Prints currently equipped items
        print "%s's currently equipped items:\n" % playerName
        
        for item in equipment:
            itemName = item.getName()
            if isinstance(item, Weapon):
                attack = item.getAttack()
                print "\tWeapon: %s." % itemName
                print "\t%s yields a %s attack bonus." % (itemName, attack)
            elif isinstance(item, Armor):
                defense = item.getDefense()
                print "\tArmor: %s." % itemName
                print "\t%s yields a %s defense bonus." % (itemName, defense)
            print ""
