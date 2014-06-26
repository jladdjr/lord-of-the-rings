#!/usr/bin/python

from monsters.monster import Monster
import constants

class WitchKing(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a WitchKing monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.WitchKing, constants.MonsterDescriptions.WitchKing, stats, constants.MonsterAttackStrings.WitchKing, constants.MonsterDeathStrings.WitchKing) 
