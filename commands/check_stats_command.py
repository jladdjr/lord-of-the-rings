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
        totalMaxHp = self._player.getTotalMaxHp()
        charmHp = self._player.getCharmHp()
        attack = self._player.getAttack()
        charmAttack = self._player.getCharmAttack()
        totalAttack = self._player.getTotalAttack()
        
        charmDefense = self._player.getCharmDefense()
        totalDefense = self._player.getTotalDefense()

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
                armorDefense = item.getDefense()
                armor = True

        #Print player stats
        print "%s's stats: \n" % name
        print "\t%s is level %s and has %s experience." % (name, level, experience)
        print "\t%s's Hp: %s/%s." % (name, hp, totalMaxHp)
        print "\t%s gets a %s HP bonus from charms." % (name, charmHp)
        print ""
        
        if weapon:
            print "\tCharacter-based attack is %s." % attack
            print "\tWeapons bonus is %s and charm bonus is %s." % (weaponsAttack, charmAttack)
            print "\tTotal attack is %s." % totalAttack
        else:
            print "\tWeapon: [Unequipped]"
        print ""
        
        if armor:
            print "\tArmor-based defense is %s." % armorDefense
            print "\tCharm-based defense is %s." % charmDefense
            print "\tTotal defense is %s." % totalDefense
        else:
            print "\tArmor:  [Unequipped]" 
                
