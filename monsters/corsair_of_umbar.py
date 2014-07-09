#!/usr/bin/python

from monsters.monster import Monster
import constants

class CorsairOfUmbar(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Corsair were pirates that preyed off of the Gondorian coasts.
    """
    def __init__(self, stats):
        """
        Initializes a CorsairOfUmbar monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.CorsairOfUmbar, constants.MonsterDescriptions.CorsairOfUmbar, \
        stats, constants.MonsterAttackStrings.CorsairOfUmbar, constants.MonsterDeathStrings.CorsairOfUmbar)