#!/usr/bin/python

from monsters.monster import Monster
import constants

class WargRider(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a WargRider monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.WargRider, constants.MonsterDescriptions.WargRider, stats, constants.MonsterAttackStrings.WargRider, constants.MonsterDeathStrings.WargRider) 
