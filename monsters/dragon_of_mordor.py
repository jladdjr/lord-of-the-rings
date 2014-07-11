#!/usr/bin/python

from monsters.monster import Monster
import constants

class DragonOfMordor(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, dragons are highly intelligent creatures.
    """
    def __init__(self, stats):
        """
        Initializes a Dragon monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.DragonOfMordor, 
        constants.MonsterDescriptions.DragonOfMordor, stats, 
        constants.MonsterAttackStrings.DragonOfMordor, 
        constants.MonsterDeathStrings.DragonOfMordor)