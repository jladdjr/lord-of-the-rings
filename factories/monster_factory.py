#!/usr/bin/python

from monsters.monster import Monster

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
        print region
        if region == 1:
            monster = Monster("Drunk hobbit", "Total j@ck@$$", 2, 2, 2)
            monsters.append(monster)
        health = difficulty * 2
        attack = difficulty * 3
        experience = difficulty
        monster = Monster("Jerk", "Total j@ck@$$", health, attack, experience)
        monsters.append(monster)

    return monsters
