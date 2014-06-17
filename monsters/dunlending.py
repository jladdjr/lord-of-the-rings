#!/usr/bin/python

from monsters.monster import Monster
import constants

class Dunlending(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a Dunlending monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Dunlending, constants.MonsterDescriptions.Dunlending, stats, constants.MonsterAttackStrings.Dunlending, constants.MonsterDeathStrings.Dunlending) 
