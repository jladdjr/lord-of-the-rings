#!/usr/bin/python

from monsters.monster import Monster
import constants

class WitchKing(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, the Witch King is the leader of the Nazgul.
    """
    def __init__(self, stats):
        """
        Initializes a WitchKing monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.WitchKing, constants.MonsterDescriptions.WitchKing, \
        stats, constants.MonsterAttackStrings.WitchKing, constants.MonsterDeathStrings.WitchKing)