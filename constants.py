#!/usr/bin/python

from monsters.troll import Troll
from monsters.nazgul import Nazgul
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin

"""
Constants for Lord of the Rings.
"""

#Game constants
COMMAND_PROMPT = "> "
CURRENCY = "rubles"

#Character initialization
STARTING_EXPERIENCE = 0
STARTING_EQUIPMENT = []
STARTING_LEVEL = 1
STARTING_MONEY = 20
STARTING_WEAPON_ATTACK = 0
STARTING_ARMOR_DEFENSE = 0

#Character stat calculation
HP_STAT = 20
ATTACK_STAT = 2
MAX_LEVEL = 20

#Items stats
SELL_LOSS_PERCENTAGE = .5
WEAPON_COST = 1
ARMOR_COST = 2

#Direction enumeration
class Direction(object):
    """
    The cardinal directions.
    """
    NORTH = 'north'
    SOUTH = 'south'
    EAST  = 'east'
    WEST  = 'west'

#Item type enumeration
class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 1, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
    ARMOR   = 2
    WEAPON  = 3
    POTION  = 4

#Region type enumeration
class RegionType(object):
    """
    The region types in Middle Earth.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 2
    HIGH_PASS     = 3
    ENEDWAITH     = 4
    EREGION       = 5
    RHOVANION     = 6
    ROHAN         = 7
    GONDOR        = 8
    MORDOR        = 9

#Region base spawn
class RegionBaseSpawn(object):
    """
    Region base spawn.
    """
    ERIADOR       = 1
    BARROW_DOWNS  = 2
    HIGH_PASS     = 3
    ENEDWAITH     = 4
    EREGION       = 5
    RHOVANION     = 6
    ROHAN         = 7
    GONDOR        = 8
    MORDOR        = 9

#Region monster distribution
class RegionMonsterDistribution(object):
    """
    Region monster distribution.
    """
    ERIADOR =     {Troll: .25,
                   Nazgul: 1}
    HIGH_PASS =   {Goblin: .8,
                   GreatGoblin: 1}

#Monster base stats
"""
Monster base stats. Stats are a 3-element list
whose elements are: hp, attack, and experience. 
"""
MONSTER_STATS = {Troll:             [1, 1, 1],
                 Nazgul:            [1, 1, 1],
                 Goblin:            [1, 1, 1],
                 GreatGoblin:       [1, 1, 1]}
    
#Battle constants
RUN_PROBABILITY_SUCCESS = .3
BATTLE_EARNINGS = 4
