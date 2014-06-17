#!/usr/bin/python

from monsters.monster import Monster
import constants

class Goblin(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Goblin monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Goblin, constants.MonsterDescriptions.Goblin, stats, constants.MonsterAttackStrings.Goblin, constants.MonsterDeathStrings.Goblin) 
