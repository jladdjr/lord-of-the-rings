#!/usr/bin/python

from monsters.monster import Monster
import constants

class Nazgul_III(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Nazgul pester the main characters throught the 
    series. Nazgul_III are tougher Nazgul that appear later in the game.
    """
    def __init__(self, stats):
        """
        Initializes a Nazgul_III monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Nazgul_III, 
        constants.MonsterDescriptions.Nazgul_III, stats, 
        constants.MonsterAttackStrings.Nazgul_III, 
        constants.MonsterDeathStrings.Nazgul_III)