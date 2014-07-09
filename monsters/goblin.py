#!/usr/bin/python

from monsters.monster import Monster
import constants

class Goblin(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, goblins are a specific type of orc.
    """
    def __init__(self, stats):
        """
        Initializes a Goblin monster. 

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.Goblin, constants.MonsterDescriptions.Goblin, \
        stats, constants.MonsterAttackStrings.Goblin, constants.MonsterDeathStrings.Goblin)