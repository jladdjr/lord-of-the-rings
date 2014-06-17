#!/usr/bin/python

from monsters.monster import Monster
import constants

class Troll(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Troll monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Troll, constants.MonsterDescriptions.Troll, stats, constants.MonsterAttackStrings.Troll, constants.MonsterDeathStrings.Troll) 
