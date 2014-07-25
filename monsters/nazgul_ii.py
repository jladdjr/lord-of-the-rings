#!/usr/bin/python

from monsters.monster import Monster
import constants

class Nazgul_II(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Nazgul pester the main characters throught the 
    series. Nazgul_II are tougher Nazgul that appear later in the game.
    """
    def __init__(self, stats):
        """
        Initializes a Nazgul_II monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Nazgul_II, 
        constants.MonsterDescriptions.Nazgul_II, stats, 
        constants.MonsterAttackStrings.Nazgul_II, 
        constants.MonsterDeathStrings.Nazgul_II)