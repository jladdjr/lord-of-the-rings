#!/usr/bin/python

from monsters.monster import Monster
import constants

class EliteUrukHai(Monster):
    """
    Inherits from Monster.
    
    These are elite Uruks warriors.
    """
    def __init__(self, stats):
        """
        Initializes a EliteUrukHai monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.EliteUrukHai, 
        constants.MonsterDescriptions.EliteUrukHai, stats, 
        constants.MonsterAttackStrings.EliteUrukHai, 
        constants.MonsterDeathStrings.EliteUrukHai)