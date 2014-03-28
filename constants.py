#!/usr/bin/python

"""
Constants for Lord of the Rings
"""

COMMAND_PROMPT = "> "

#Character initialization
STARTING_EXPERIENCE = 0
STARTING_EQUIPMENT = []
STARTING_LEVEL = 1
STARTING_MONEY = 20

#Character stat calculation
HP_STAT = 20
ATTACK_STAT = 2

#Direction enumeration
class Direction(object):
    """
    The cardinal directions.
    """
    NORTH = 'north'
    SOUTH = 'south'
    EAST  = 'east'
    WEST  = 'west'

#Type enumeration
class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 1, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
    ARMOR   = 2
    WEAPON  = 3
    POTION  = 4

