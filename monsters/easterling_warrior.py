#!/usr/bin/python

from monsters.monster import Monster
import constants

class EasterlingWarrior(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, easterlings are the inhabitants of people east of
    Middle Earth. 
    """
    def __init__(self, stats):
        """
        Initializes a EasterlingWarrior monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.EasterlingWarrior, constants.MonsterDescriptions.EasterlingWarrior, \
        stats, constants.MonsterAttackStrings.EasterlingWarrior, constants.MonsterDeathStrings.EasterlingWarrior)