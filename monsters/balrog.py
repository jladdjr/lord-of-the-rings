#!/usr/bin/python

from monsters.monster import Monster
import constants

class Balrog(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Balrog monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Balrog, constants.MonsterDescriptions.Balrog, stats, constants.MonsterAttackStrings.Balrog, constants.MonsterDeathStrings.Balrog) 
