#!/usr/bin/python

from monsters.monster import Monster
import constants

class WargRider(Monster):
    """
    Inherits from Monster.
    
    In Tolkien's universe, wargs are a race of wild wolves. Warg 
    riders are orc-mounted wargs.
    """
    def __init__(self, stats):
        """
        Initializes a WargRider monster.

        @param stats:     3-element list of Monster stats including attack, hp,
                          and experience (in that order).
        """
        Monster.__init__(self, constants.MonsterNames.WargRider, constants.MonsterDescriptions.WargRider, \
        stats, constants.MonsterAttackStrings.WargRider, constants.MonsterDeathStrings.WargRider)