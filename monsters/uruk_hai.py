#!/usr/bin/python

from monsters.monster import Monster
import constants

class UrukHai(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a UrukHai monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.UrukHai, constants.MonsterDescriptions.UrukHai, stats, constants.MonsterAttackStrings.UrukHai, constants.MonsterDeathStrings.UrukHai) 
