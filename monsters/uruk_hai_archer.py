#!/usr/bin/python

from monsters.monster import Monster
import constants

class UrukHaiArcher(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a UrukHaiArcher monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.UrukHaiArcher, constants.MonsterDescriptions.UrukHaiArcher, stats, constants.MonsterAttackStrings.UrukHaiArcher, constants.MonsterDeathStrings.UrukHaiArcher) 
