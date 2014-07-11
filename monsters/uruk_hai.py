#!/usr/bin/python

from monsters.monster import Monster
import constants

class UrukHai(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Uruk Hai were a cross-breed of men and orcs.
    """
    def __init__(self, stats):
        """
        Initializes a UrukHai monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.UrukHai, 
        constants.MonsterDescriptions.UrukHai, stats, 
        constants.MonsterAttackStrings.UrukHai, 
        constants.MonsterDeathStrings.UrukHai)