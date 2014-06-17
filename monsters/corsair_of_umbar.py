#!/usr/bin/python

from monsters.monster import Monster
import constants

class CorsairOfUmbar(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a CorsairOfUmbar monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.CorsairOfUmbar, constants.MonsterDescriptions.CorsairOfUmbar, stats, constants.MonsterAttackStrings.CorsairOfUmbar, constants.MonsterDeathStrings.CorsairOfUmbar) 
