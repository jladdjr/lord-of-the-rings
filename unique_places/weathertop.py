#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from battle_engine import battle
import constants
import random

class Weathertop(UniquePlace):
    """
    An unique place in .
    """
    def __init__(self, name, description, greetings):
        """
        Initialize UniquePlace object.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
	@param greetings:	The greetings the user gets as he enters the inn.        
	"""
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        self._monsters = []
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._monsters.append(nazgul)
                
    def enter(self, player):
        """
        Enter Weathertop.

        @param player:  The current player.
        """
        print self._greetings
        print ""
        print "Even though you have no personal connection with the place, you feel a strong sense of nostalgia and belong at Weathertop."
        raw_input("Press enter to continue.")

        #User given choice to camp at Weathertop
        print \
"""
Would you like to camp at the Weathertop?
\t\"Yes I would like to camp.\"       - 'camp'
\t\"No I would like to keep moving.\" - 'keep moving'
""" 
        choice = None
        acceptable = ["camp", "keep moving"]
        while choice not in acceptable:
            choice = raw_input("Choice? ")
            if choice == "camp":
                self._camp(player)
            elif choice == "keep moving":
                return
            else:
                print "Huh?"

    def _camp(self, player):
        """
        What happens if player camps.
        Chance of random encounter by Nazgul.
        """
        #Chance random Nazgul attack
        if random.random() < .3:
            print "As you prepare your camping gear, you hear some rustling in the shadows...."
            battle(player, constants.BattleEngineContext.STORY, self._monsters, run = False)
            
        #Peaceful rest
        else:
            print "You enjoy a relaxing stay at atop ancient ruins."
            amountHealing = player.getMaxHp() - player.getHp()
            player.heal(amountHealing)
            print "You wake up relaxed and ready to go!"
            
