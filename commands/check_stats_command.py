#!/usr/bin/python

from command import Command
from items.weapon import Weapon
from items.armor import Armor
from items.charm import Charm

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
        
        #Get HP stats
        hp = self._player.getHp()
        charmHp = self._player.getCharmHp()
        totalMaxHp = self._player.getTotalMaxHp()
        
        #Get attack stats
        attack = self._player.getAttack()
        charmAttack = self._player.getCharmAttack()
        totalAttack = self._player.getTotalAttack()
        
        #Get defense stats
        charmDefense = self._player.getCharmDefense()
        totalDefense = self._player.getTotalDefense()

        #Create defaults - for determining of weapon and armor exist
        weapon = None
        armor = None
        charm = None
        
        #Get equipment bonuses
        equipment = self._player.getEquipped()
        equipmentList = equipment.getItems()
        for item in equipmentList:
            if isinstance(item, Weapon):
                weaponsAttack = item.getAttack()
                weapon = True
            if isinstance(item, Armor):
                armorDefense = item.getDefense()
                armor = True

        #Print player stats
        print "%s's stats: \n" % name
        print "\t%s is level %s and has %s experience." % (name, level, experience)
        print "\t%s's HP: %s/%s." % (name, hp, totalMaxHp)
        print "\t%s gets a %s HP bonus from charms." % (name, charmHp)
        print ""
        
        #For player weapon
        if weapon:
            print "\tCharacter-based attack is %s." % attack
            print "\tWeapons bonus is %s and charm bonus is %s." % (weaponsAttack, charmAttack)
            print "\tTotal attack is %s." % totalAttack
        else:
            print "\tWeapon: [Unequipped]."
        print ""
        
        #For player armor
        if armor:
            print "\tArmor-based defense is %s." % armorDefense
            print "\tCharm-based defense is %s." % charmDefense
            print "\tTotal defense is %s." % totalDefense
        else:
            print "\tArmor:  [Unequipped]" 
        print ""