#!/usr/bin/python

from monsters.monster import Monster
import constants

class BlackNumernorian_II(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Black Numernorians were powerful occultists.
    """
    def __init__(self, stats):
        """
        Initializes a BlackNumernorian_II monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.BlackNumernorian_II, 
        constants.MonsterDescriptions.BlackNumernorian_II, stats, 
        constants.MonsterAttackStrings.BlackNumernorian_II, 
        constants.MonsterDeathStrings.BlackNumernorian_II)