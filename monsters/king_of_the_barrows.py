#!/usr/bin/python

from monsters.monster import Monster
import constants

class KingOfTheBarrows(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, the King of the Barrows is the Chief spirit over the Downs.
    """
    def __init__(self, stats):
        """
        Initializes a King of the Barrows monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.KingOfTheBarrows, constants.MonsterDescriptions.KingOfTheBarrows, \
        stats, constants.MonsterAttackStrings.KingOfTheBarrows, constants.MonsterDeathStrings.KingOfTheBarrows)