#!/usr/bin/python

from monsters.monster import Monster
import constants

class GreatGoblin(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, the Great Goblin is the leader of the 
    goblin of High Pass.
    """
    def __init__(self, stats):
        """
        Initializes a Great Goblin monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.GreatGoblin, 
        constants.MonsterDescriptions.GreatGoblin, stats, 
        constants.MonsterAttackStrings.GreatGoblin, 
        constants.MonsterDeathStrings.GreatGoblin)