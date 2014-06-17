#!/usr/bin/python

from monsters.monster import Monster
import constants

class Dragon(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Dragon monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Dragon, constants.MonsterDescriptions.Dragon, stats, constants.MonsterAttackStrings.Dragon, constants.MonsterDeathStrings.Dragon) 
