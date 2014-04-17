#!/usr/bin/python

from command import Command

class UnequipCommand(Command):
    """
    Unequips player with currently equipped item.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new unequip command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Unequips player with item in inventory.
        """
        itemToUnequip = raw_input("Which item do you want to unequip? \n")
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        
        itemInventory = inventory.getItemByName(itemToUnequip)
        itemEquipment = equipped.getItemByName(itemToUnequip)
        
        #Checks if item is in inventory and is currently equipped
        if not itemInventory:
            print "%s is not in your inventory!" % itemToUnequip
            return
        
        if not itemEquipment:
            print "%s is not currently equipped!" % itemToUnequip
            return

        #Equips player with item
        self._player.unequip(itemEquipment)
