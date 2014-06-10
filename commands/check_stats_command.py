#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor

class CheckStatsCommand(Command):
    """
    Displays player stats.
    """
    def __init__(self, name, explanation, player):
        """
        Initializes new check stats command.

        @param name:         Command name.
        @param explanation:  Explanation of command.
        @param player:       The player object.
        """
        #Call parent's init method
        Command.__init__(self, name, explanation)

        self._player = player

    def execute(self):
        """
        Displays player stats.
        """
        #Get player stats
        name = self._player.getName()
        experience = self._player.getExperience()
        level = self._player.getLevel()
        
        hp = self._player.getHp()
        attack = self._player.getAttack()
        totalAttack = self._player.getTotalAttack()

        #Create defaults - for determining of weapon and armor exist
        weapon = None
        armor = None

        #Get equipment bonuses
        equipment = self._player.getEquipped()
        equipmentList = equipment.getItems()
        for item in equipmentList:
            if isinstance(item, Weapon):
                weaponsAttack = item.getAttack()
                weapon = True
            elif isinstance(item, Armor):
                defense = item.getDefense()
                armor = True

        #Print player stats
        print "%s's stats: \n" % name
        print "\t%s is level %s and has %s experience." % (name, level, experience)
        print "\t%s's Hp: %s." % (name, hp)
        print ""
        if weapon:
            print "\tCharacter-based attack is %s; weapons bonus is %s." % (attack, weaponsAttack)
            print "\tTotal attack is %s." % totalAttack
        else:
            print "\tWeapon: [Unequipped]"
        if armor:
            print "\tArmor-based defense is %s." % defense
        else:
            print "\tArmor:  [Unequipped]" 
                
