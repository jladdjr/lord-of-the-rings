#!/usr/bin/python

from monsters.monster import Monster
import constants

class Sauroman(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Sauroman was the chief of the wizards 
    of Middle Earth.
    """
    def __init__(self, stats):
        """
        Initializes a Sauroman monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Sauroman, constants.MonsterDescriptions.Sauroman, \
        stats, constants.MonsterAttackStrings.Sauroman, constants.MonsterDeathStrings.Sauroman)