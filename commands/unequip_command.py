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

        #Finish initializing help-specific settings
        self._player = player

    def execute(self):
        """
        Unequips player with item in inventory.
        """
        itemToEquip = raw_input("Which item do you want to unequip? \n")
        inventory = self._player.getInventory()
        equipped = self._player.getEquipped()
        
        itemInventory = inventory.getItemByName(itemToEquip)
        itemEquipment = equipped.getItemByName(itemToEquip)
        
        #Checks if item is in inventory and is currently equipped
        if not itemInventory:
            print "%s is not in your inventory!" %(itemToEquip)
            return
        
        if not itemEquipment:
            print "%s is not currently equipped!" %(itemToEquip)
            return

        #Equips player with item
        player.unequip(itemToEquip)
