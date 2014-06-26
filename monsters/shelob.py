#!/usr/bin/python

from monsters.monster import Monster
import constants

class Shelob(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Shelob monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Shelob, constants.MonsterDescriptions.Shelob, stats, constants.MonsterAttackStrings.Shelob, constants.MonsterDeathStrings.Shelob) 
