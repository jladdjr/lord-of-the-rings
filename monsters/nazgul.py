#!/usr/bin/python

from monsters.monster import Monster
import constants

class Nazgul(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Nazguls pester the main characters throught the 
    series.
    """
    def __init__(self, stats):
        """
        Initializes a Nazgul monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Nazgul, constants.MonsterDescriptions.Nazgul, \
        stats, constants.MonsterAttackStrings.Nazgul, constants.MonsterDeathStrings.Nazgul)