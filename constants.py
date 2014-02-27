"""
Constants for Lord of the Rings
"""

COMMAND_PROMPT = "> "


#Character stats
STARTING_LEVEL = 1
STARTING_EXPERIENCE = 0

#TODO: Stats are not constants (they change over the course of the game)
#      Need to create a separate GameStats class to maintain this information. -JDL

attackStat = 2
hpStat = 10

#Type enumeration
class ItemType(object):
    """
    When a new item is created, its type should
    be added here. (e.g. POTION = 2, WEAPON = 2, ARMOR = 3, etc.)
    """
    GENERIC = 1
    ARMOR   = 2
    WEAPON  = 3

