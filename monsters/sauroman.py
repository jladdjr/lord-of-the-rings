#!/usr/bin/python

from monsters.monster import Monster
import constants

class Sauroman(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Sauroman monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Sauroman, constants.MonsterDescriptions.Sauroman, stats, constants.MonsterAttackStrings.Sauroman, constants.MonsterDeathStrings.Sauroman) 