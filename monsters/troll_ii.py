#!/usr/bin/python

from monsters.monster import Monster
import constants

class Troll_II(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, these were beasts of great strength but 
    poor intellect.
    """
    def __init__(self, stats):
        """
        Initializes a Troll_II monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Troll_II, 
        constants.MonsterDescriptions.Troll_II, stats, 
        constants.MonsterAttackStrings.Troll_II, 
        constants.MonsterDeathStrings.Troll_II)