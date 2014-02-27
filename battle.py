#!/usr/bin/python

import random
from monster import Monster
from monsters import Monsters

class Battle(object):
    """
    A battle sequence for Lord of the Rings
    """

    def __init__(self):
        """
        Initializes the battle sequence
        """
        monsters = Monsters()
        
        numberMonsters = random.randrange(3, 10)
        for monster in numberMonsters:
            specificMonster = Monster()
            monsters.addMonster(specificMonster)

    def battleSequence(self):
        while monsters.count() != 0 and ###player isn't defeated###:
            menu =
            """
            You are at battle with %s monsters!
            1) Attack
            2) Item
            3) Run
            """ %(monsters.count())
            print menu

            choice = None
            if choice == 1:
                ###Player attacks monster###
            elif choice == 2:
                ###Item used###
            else:
                ###Depending on difficulty of monsters probability sequence which allows battle to end###
            ###monsters attack back###

    def endSequence(self):
        ###Congradulate player if player won. Otherwise end game sequence?###
        ###Give party members whose health>0 experience.
        ###Exit the battle object
