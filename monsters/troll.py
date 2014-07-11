#!/usr/bin/python

from monsters.monster import Monster
import constants

class Troll(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, these were beasts of great strength but 
    poor intellect.
    """
    def __init__(self, stats):
        """
        Initializes a Troll monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Troll, 
        constants.MonsterDescriptions.Troll, stats, 
        constants.MonsterAttackStrings.Troll, 
        constants.MonsterDeathStrings.Troll)