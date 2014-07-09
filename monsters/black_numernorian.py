#!/usr/bin/python

from monsters.monster import Monster
import constants

class BlackNumernorian(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Black Numernorians were powerful occultists.
    """
    def __init__(self, stats):
        """
        Initializes a BlackNumernorian monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.BlackNumernorian, constants.MonsterDescriptions.BlackNumernorian, \
        stats, constants.MonsterAttackStrings.BlackNumernorian, constants.MonsterDeathStrings.BlackNumernorian)