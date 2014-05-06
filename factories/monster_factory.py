#!/usr/bin/python

from monsters.monster import Monster

def getMonster(number, region, difficulty):
    """
    Generates enemies for the battle sequence.

    @param number:      The number of monsters to generate.
    @param type:        The type of monsters to generate.
    @param difficulty:  The number of enemies to generate.
    """
    monsters = []

    #Spawn monsters
    for monster in range(number):
        health = difficulty * 2
        attack = difficulty * 3
        experience = difficulty
        monster = Monster("Jerk", "Total j@ck@$$", monsterHealth, monsterAttack, experience)
        monsters.append(monster)

    return monsters
