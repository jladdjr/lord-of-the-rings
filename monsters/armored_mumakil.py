#!/usr/bin/python

from monsters.monster import Monster
import constants

class ArmoredMumakil(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a ArmoredMumakil monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.ArmoredMumakil, constants.MonsterDescriptions.ArmoredMumakil, stats, constants.MonsterAttackStrings.ArmoredMumakil, constants.MonsterDeathStrings.ArmoredMumakil) 
