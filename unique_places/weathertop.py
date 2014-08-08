#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from battle_engine import battle
import constants
import random

class Weathertop(UniquePlace):
    """
    A unique place in Weather Hills. Here the user is given the option to camp.
    If the user decides to camp, there is a chance that he gets attacked by
    Nazgul. If this does not happen, player gets healed up to full health.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Weathertop.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Generates Nazgul wave
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
        
        print ("Even though you have no personal connection with the place,"
        " you \nfeel a strong sense of nostalgia at Weathertop.")
        raw_input("Press enter to continue. ")

        #Solicit user input
        choice = self._choice()
            
        #Run user-dependent sequence
        if choice == "camp":
            self._camp(player)
        elif choice == "keep moving":
            print "You continue in your quest."
            print ""

    def _choice(self):
        """
        Solicits user choice
        """
        print \
"""
You are spent after a day of travel. Would you like
to camp the night at Weathertop?
\t\"Yes I would like to camp.\"       - 'camp'
\t\"No I would like to keep moving.\" - 'keep moving'
""" 
        choice = None
        acceptable = ["camp", "keep moving"]
        while choice not in acceptable:
            choice = raw_input("Choice? ")
        print ""
        
        return choice
        
    def _camp(self, player):
        """
        The camping action sequence. One of two things happen:
        -User gets attacked by a group of Nazgul.
        -Player spends the night undisturbed and gets fully healed.
        """
        #Nazgul encounter
        if random.random() < constants.WEATHERTOP_BATTLE_PROB:
            print ("As you prepare your camping gear, you hear some rustling" 
            " in the \nshadows....")
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._monsters)
            if not result:
                return
                
            print ("Alas, peaceful rest was never to be. After all, you are a" 
            " man being \nhunted.")
            print ""
            
        #Peaceful rest
        else:
            print "You enjoy a relaxing stay among ancient ruins."
            amountHealing = player.getMaxHp() - player.getHp()
            player.heal(amountHealing)
            print "You wake up relaxed and ready to go!"
            print ""