#!/usr/bin/python

from monsters.monster import Monster
import constants

class Shelob(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Shelob is an enormous spider who 
    lives in Cirith Ungol.
    """
    def __init__(self, stats):
        """
        Initializes a Shelob monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Shelob, constants.MonsterDescriptions.Shelob, \
        stats, constants.MonsterAttackStrings.Shelob, constants.MonsterDeathStrings.Shelob)