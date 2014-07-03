#!/usr/bin/python

from monsters.monster import Monster
import constants

class OrcArcher(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a OrcArcher monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.OrcArcher, constants.MonsterDescriptions.OrcArcher, stats, constants.MonsterAttackStrings.OrcArcher, constants.MonsterDeathStrings.OrcArcher) 
