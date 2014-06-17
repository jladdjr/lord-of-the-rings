#!/usr/bin/python

from monsters.monster import Monster
import constants

from math import floor
import random

def getMonsters(number, region, bonusDifficulty):
    """
    Generates enemies for the battle sequence.

    @param number:      The number of monsters to generate.
    @param region:      The region of the map Player is currently in.
    @param difficulty:  The number of enemies to generate.
    """
    monsters = []
    monsterDistribution = constants.REGIONAL_MONSTER_DISTRIBUTION[region]

    for numSpawn in range(number):
        randomNum = random.random()
        for Monster in monsterDistribution:
            lowerLimit = monsterDistribution[Monster][0]
            upperLimit = monsterDistribution[Monster][1]
            if lowerLimit <= randomNum < upperLimit:
                #Find monster stats
                stats = constants.MONSTER_STATS[Monster]
                #Modify monster stats for bonusDifficulty
                modifiedStats = []
                for stat in stats:
                    modifiedStat = stat * (1 + bonusDifficulty)
                    modifiedStat = floor(modifiedStat)
                    modifiedStats.append(modifiedStat)
                #Instantiate and append monster to monsters
                monsterSpawn = Monster(modifiedStats)
                monsters.append(monsterSpawn)
                #There should only be one monster spawned per iteration
                break
    
    return monsters
