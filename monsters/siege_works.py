#!/usr/bin/python

from monsters.monster import Monster
import constants

class SiegeWorks(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a SiegeWorks monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.SiegeWorks, constants.MonsterDescriptions.SiegeWorks, stats, constants.MonsterAttackStrings.SiegeWorks, constants.MonsterDeathStrings.SiegeWorks) 
