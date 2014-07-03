#!/usr/bin/python

from monsters.monster import Monster
import constants

class Orc(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Orc monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Orc, constants.MonsterDescriptions.Orc, stats, constants.MonsterAttackStrings.Orc, constants.MonsterDeathStrings.Orc) 
