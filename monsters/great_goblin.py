#!/usr/bin/python

from monsters.monster import Monster
import constants

class GreatGoblin(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Great Goblin monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.GreatGoblin, constants.MonsterDescriptions.GreatGoblin, stats, constants.MonsterAttackStrings.GreatGoblin, constants.MonsterDeathStrings.GreatGoblin)       
