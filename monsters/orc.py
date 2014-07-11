#!/usr/bin/python

from monsters.monster import Monster
import constants

class Orc(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, orcs serve as the bulk of Sauron's army.
    """
    def __init__(self, stats):
        """
        Initializes a Orc monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Orc, 
        constants.MonsterDescriptions.Orc, stats, 
        constants.MonsterAttackStrings.Orc, 
        constants.MonsterDeathStrings.Orc)