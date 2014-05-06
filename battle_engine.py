#!/usr/bin/python

from factories.monster_factory import getMonsters

class doBattle(self, player):
    """
    Battle engine for Lord of the Rings
    """
    location = player.getLocation()
    monsterDifficulty = location.getDifficulty()

    number = 3 * monsterDifficulty
    region = "Doesn't matter right now"
    difficulty = monsterDifficulty
    
    monsters = spawnMonsters(number, region, difficulty)

    print "OMG MONSTER BATTLE HAPPENEDZ."
    print "U R BATTLING",monsters
    #Spawns enemies
    #Simple battle
    #Reward player - exp, money, items
    
