#!/usr/bin/python

from monsters.monster import Monster
import constants

class MouthOfSauron(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Black Gate monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.MouthOfSauron, constants.MonsterDescriptions.MouthOfSauron, stats, constants.MonsterAttackStrings.MouthOfSauron, constants.MonsterDeathStrings.MouthOfSauron)