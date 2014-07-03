#!/usr/bin/python

from monsters.monster import Monster
import constants

class UrukHaiElite(Monster):
    """
    A type of Monster.
    """
    def __init__(self, stats):
        """
        Initializes a UrukHaiElite monster. Inherits from Monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.UrukHaiElite, constants.MonsterDescriptions.UrukHaiElite, stats, constants.MonsterAttackStrings.UrukHaiElite, constants.MonsterDeathStrings.UrukHaiElite) 
