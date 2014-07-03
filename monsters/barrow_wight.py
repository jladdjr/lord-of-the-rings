#!/usr/bin/python

from monsters.monster import Monster
import constants

class BarrowWight(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Barrow Wight monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.BarrowWight, constants.MonsterDescriptions.BarrowWight, stats, constants.MonsterAttackStrings.BarrowWight, constants.MonsterDeathStrings.BarrowWight) 
