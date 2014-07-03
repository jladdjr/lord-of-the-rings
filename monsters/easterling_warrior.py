#!/usr/bin/python

from monsters.monster import Monster
import constants

class EasterlingWarrior(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a EasterlingWarrior monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.EasterlingWarrior, constants.MonsterDescriptions.EasterlingWarrior, stats, constants.MonsterAttackStrings.EasterlingWarrior, constants.MonsterDeathStrings.EasterlingWarrior) 
