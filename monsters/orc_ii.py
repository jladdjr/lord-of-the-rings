#!/usr/bin/python

from monsters.monster import Monster
import constants

class Orc_II(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, orcs serve as the bulk of Sauron's army.
    """
    def __init__(self, stats):
        """
        Initializes a Orc_II monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Orc_II, 
        constants.MonsterDescriptions.Orc_II, stats, 
        constants.MonsterAttackStrings.Orc_II, 
        constants.MonsterDeathStrings.Orc_II)