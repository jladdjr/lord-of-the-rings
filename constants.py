"""
Constants.
"""

COMMAND_PROMPT = "> "


class Direction(object):
    """
    The cardinal directions.
    """
    NORTH = 'north'
    SOUTH = 'south'
    EAST  = 'east'
    WEST  = 'west'


class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 2, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
