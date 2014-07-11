#!/usr/bin/python

from command import Command
from items.potion import Potion
from items.item_set import ItemSet

class UsePotionCommand(Command):
    """
    Allows player to use potion out of combat.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes use potion command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Uses potion in inventory to heal player.
        """
        #Check that potions in inventory
        inventory = self._player.getInventory()
        potions = ItemSet()
        
        for item in inventory:
            if isinstance(item, Potion):
                potions.addItem(item)
        if potions.count() == 0:
            print "%s has no potions." % self._player.getName()
            return
        
        #User prompt
        print "%s currently has:" % self._player.getName()
        for potion in potions:
            print "\t%s with %s healing power." % (potion.getName(), 
            potion.getHealing())
        print ""
    
        choice = None
        while True:
            choice = raw_input("Which potion would you like to use? ")
            if potions.containsItemWithName(choice):
                break
            else:
                print "%s does not have that potion." % self._player.getName()
                print ""

        #Healing mechanics
        potionChoice = potions.getItemByName(choice)
        healing = potionChoice.getHealing()
        
        preHealedHealth = self._player.getHp()
        self._player.heal(healing)
        postHealedHealth = self._player.getHp()
        healed = postHealedHealth - preHealedHealth
        
        inventory.removeItem(potionChoice)
        
        print "%s was healed by %s! %s's health is now %s." \
        % (self._player.getName(), healed, self._player.getName(), 
        self._player.getHp())