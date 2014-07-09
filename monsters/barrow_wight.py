#!/usr/bin/python

from monsters.monster import Monster
import constants

class BarrowWight(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Barrow Wights were evil spirits that inhabited the Downs.
    """
    def __init__(self, stats):
        """
        Initializes a Barrow Wight monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.BarrowWight, constants.MonsterDescriptions.BarrowWight, \
        stats, constants.MonsterAttackStrings.BarrowWight, constants.MonsterDeathStrings.BarrowWight)