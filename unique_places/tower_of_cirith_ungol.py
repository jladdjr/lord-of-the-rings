#!/usr/bin/python

from unique_place import UniquePlace
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.shelob import Shelob
from battle_engine import battle
from items.unique_items import phialOfGaladriel
import constants

import random

class TowerOfCirithUngol(UniquePlace):
    """
    The Tower of Cirith Ungol is a unique place in Cirith Ungol. The Tower of
    Cirith Ungol is a fortress that guards the Cirith Ungol pass.

    If a player visits the Tower, he has a chance to fight Shelob and then 
    monsters from the fortress itself.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize Tower of Cirith Ungol.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)
        
        self._wave = []
        self._wave2 = []
        
        #Create monster wave #1
        monster = Shelob(constants.MONSTER_STATS[Shelob])
        self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(15):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave2.append(monster)
            
    def enter(self, player):
        """
        The action sequence for Tower of Cirith Ungol.
        
        @param player:   The current player.
        """
        #Story
        print self._greetings
        print ""
        
        print ("As you climb the path of Cirith Ungol, you stare at the"
            " ghastly city of Minas \nMorgul.")
        raw_input("Press enter to continue. ")
        print ""
        
        #Solicit user choice
        choice = self._choice()
        
        #Action sequences given user choice
        if choice == "yes":
            self._shelobClef(player)
        else:
            print "You live to fight another day."
            print ""
            return
        
    def _choice(self):
        """
        Determines if user wants to attack or run.
        """
        #Solicit user choice
        print "To continue, you must go through the Shelob's Clef."
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = raw_input("Would you like to continue? Choices:"
                " 'yes' and 'no.' ")
        print ""
        
        return choice

    def _shelobClef(self, player):
        """
        Action sequence for venturing through Shelob's Clef.
        
        @param player:   The player object.
        """
        #Story
        print ("As you enter into Shelob's Clef, you are surrounded by a"
            " supernatural darkness and \nthe stench of rotting corpses.")
        raw_input("Press enter to continue. ")
        print ""
        
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        #If Phial of Galadriel in inventory
        if phialOfGaladriel in player.getInventory():
            print "Galadriel's phial lights up the entire chamber."
            raw_input("Press enter to continue. ")
            print ""
            
            print ("The light gives you strength... and Shelob backs away,"
            " afraid of the light.")
            raw_input("Press enter to continue. ")
            print ""
            
            #Call next action sequence
            self._cirithUngol(player)
        
        #A potential encounter with Shelob
        shelobAppearance = random.random()
        if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave)
            if not result:
                return
            
        print "You encounter a thick spider web."
        raw_input("Press enter to hack through the web. ")
        print ""
        
        #A potential encounter with Shelob
        shelobAppearance = random.random()
        if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave)
            if not result:
                return
                
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        #A potential encounter with Shelob
        shelobAppearance = random.random()
        if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
            result = battle(player, constants.BattleEngineContext.STORY, self._wave)
            if not result:
                return
                
        print "You encounter a thick spider web."
        raw_input("Press enter to hack through the web. ")
        print ""
        
        #A potential encounter with Shelob
        shelobAppearance = random.random()
        if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave)
            if not result:
                return
                
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        #A potential encounter with Shelob
        shelobAppearance = random.random()
        if shelobAppearance < constants.CIRITH_UNGOL_SHELOB_PROB:
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave)
            if not result:
                return
                
        print "You have emerged through the darkness!"
        raw_input("Press enter to continue. ")
        print ""
        
        #Call next action sequence
        self._cirithUngol(player)
    
    def _cirithUngol(self, player):
        """
        Action sequence for the Tower of Cirith Ungol.
        
        @param player:   The player object.
        """
        successfulEscape = random.random()
        #If player manages to escape undetected
        if successfulEscape < constants.CIRITH_UNGOL_EVASION_PROB:
            print ("You manage to sneak through the Tower of Cirith Ungol and"
                " are now in the heart \nof Mordor.")
            raw_input("Press enter to continue. ")
            print ""
        #If player gets detected
        else:
            print ("As you attempt to sneak through the rest of the passage,"
                " you are discovered \nby an orc patrol.")
            raw_input("Press enter to continue. ")
            print ""
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._wave2)
            if not result:
                return
                
            #Story
            print ("You make it into Mordor and Sauron has been alerted of"
                " your presence.")
            raw_input("Press enter to continue. ")
            print ""
        
        #Create port for quest completion
        self._createPort("east")