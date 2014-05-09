#!/usr/bin/python

from monsters.monster import Monster
from constants import RegionType

def getMonsters(number, region, difficulty):
    """
    Generates enemies for the battle sequence.

    @param number:      The number of monsters to generate.
    @param region:      The region of the map Player is currently in.
    @param difficulty:  The number of enemies to generate.
    """
    monsters = []

    #Spawn monsters
    for monster in range(number):
        if region == RegionType.ERIADOR:
            pass
        elif region == RegionType.HIGH_PASS:
            pass
        elif region == RegionType.ENEDWAITH:
            pass
        elif region == RegionType.RHOVANION:
            pass
        elif region == RegionType.ROHAN:
            pass
        elif region == RegionType.GONDOR:
            pass
        elif region == RegionType.MORDOR:
            pass
        else:
            errorMsg = "Unsupported region type for monster spawn."
            raise AssertionError(errorMsg)
        health = difficulty * 2
        attack = difficulty * 3
        experience = difficulty
        monster = Monster("Jerk", "Total j@ck@$$", health, attack, experience)
        monsters.append(monster)

    return monsters
