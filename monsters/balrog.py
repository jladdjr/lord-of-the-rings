#!/usr/bin/python

from monsters.monster import Monster
import constants

class Balrog(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, Balrog were some of the deadliest beings in Middle 
    Earth.
    """
    def __init__(self, stats):
        """
        Initializes a Balrog monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Balrog, 
        constants.MonsterDescriptions.Balrog, stats, 
        constants.MonsterAttackStrings.Balrog, 
        constants.MonsterDeathStrings.Balrog)