#!/usr/bin/python

from monsters.monster import Monster
import constants

class MouthOfSauron(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, the Mouth of Sauron is the chief 
    ambassador of Sauron.
    """
    def __init__(self, stats):
        """
        Initializes a Mouth of Sauron monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.MouthOfSauron, constants.MonsterDescriptions.MouthOfSauron, \
        stats, constants.MonsterAttackStrings.MouthOfSauron, constants.MonsterDeathStrings.MouthOfSauron)