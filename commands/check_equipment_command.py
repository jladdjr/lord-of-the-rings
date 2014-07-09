#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm

class CheckEquipmentCommand(Command):
    """
    Displays player equipment and details equipment stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check equipment command.

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
        playerName = self._player.getName()
        equipment = self._player.getEquipped()
        
        sortedEquipment = self._sortEquipment(equipment)
        
        #Prints currently equipped items
        print "%s's currently equipped items:\n" % playerName
        
        for item in sortedEquipment:
            itemName = item.getName()
            if isinstance(item, Weapon):
                attack = item.getAttack()
                print "\tWeapon: %s." % itemName
                print "\t%s yields a %s attack bonus." % (itemName, attack)
            elif isinstance(item, Armor):
                defense = item.getDefense()
                print "\tArmor: %s." % itemName
                print "\t%s yields a %s defense bonus." % (itemName, defense)
            elif isinstance(item, Charm):
                attack = item.getAttack()
                defense = item.getDefense()
                hp = item.getHp()
                print "\tCharm: %s:" % itemName
                if item.getAttack():
                    print "\t%s yields a %s attack bonus." % (itemName, attack)
                if item.getDefense():
                    print "\t%s yields a %s defense bonus." % (itemName, defense)
                if item.getHp():
                    print "\t%s yields a %s HP bonus." % (itemName, hp)
            else:
                errorMsg = "CheckEquipmentCommand command given invalid item type."
                raise AssertionError(errorMsg)
            print ""
            
    def _sortEquipment(self, equipment):
        """
        Sorts player equipment.
        
        @param equipment:     Player equipped object.
        """
        sortedEquipment = []
        
        #Sorts items
        for item in equipment:
            if isinstance(item, Weapon):
                sortedEquipment.append(item)
        for item in equipment:
            if isinstance(item, Armor):
                sortedEquipment.append(item)
        for item in equipment:
            if isinstance(item, Charm):
                sortedEquipment.append(item)
                
        return sortedEquipment