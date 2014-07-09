#!/usr/bin/python

from monsters.monster import Monster
import constants

class Dunlending(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Dunlendings were the original men of Middle Earth.
    """
    def __init__(self, stats):
        """
        Initializes a Dunlending monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Dunlending, constants.MonsterDescriptions.Dunlending, \
        stats, constants.MonsterAttackStrings.Dunlending, constants.MonsterDeathStrings.Dunlending)