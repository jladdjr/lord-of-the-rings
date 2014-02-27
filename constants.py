"""
Constants for Lord of the Rings
"""

COMMAND_PROMPT = "> "

#Character stats
startingLevel = 1
startingExperience = 0

attackStat = 2
hpStat = 10

#Type enumeration
class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 2, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
    ARMOR = 2
    WEAPON = 3

