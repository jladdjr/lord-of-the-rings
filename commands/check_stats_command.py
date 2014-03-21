#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor

class CheckStatsCommand(Command):
    """
    Prints player stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check stats command.

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
        Displays player stats.
        """
        name = self._player.getName()
        experience = self._player.getExperience()
        level = self._player.getLevel()
        
        hp = self._player.getHp()
        attack = self._player.getAttack()
        weaponsAttack = 0
        defense = 0
        
        equipment = self._player.getEquipped()
        equipmentList = equipment.getItems()
        for item in equipmentList:
            if isinstance(item, Armor):
                defense = item.getDefense()
            elif isinstance(item, Weapon):
                weaponsAttack = item.getAttack()
                
        total = attack + weaponsAttack
                
        print "%s's stats: \n" %name
        print "%s is level %s and has %s experience." %(name, level, experience)
        print "Hp: %s" %hp
        print "Armor-based defense is %s" %defense
        print "Character-based attack is %s; weapons bonus is %s for a total of %s" %(attack, weaponsAttack, total)
        
