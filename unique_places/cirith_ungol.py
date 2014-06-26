#!/usr/bin/python

from unique_place import UniquePlace
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.shelob import Shelob
from battle_engine import battle
from items.unique_items import phialOfGaladriel
import constants

import random

class CirithUngol(UniquePlace):
    """
    An instance of UniquePlace.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize UniquePlace object.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters the inn.        
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
        Enter Cirith Ungol.
        
        @param player:   The current player.
        """
        print self._greetings
        print ""
        
        print "As you climb the path of Cirith Ungol, you stare at the ghastly city of Minas Morgul."
        raw_input("Press enter to continue. ")
        print ""
        
        choice = self._choice()
        if choice == "yes":
            self._shelobClef(player)
        else:
            print "You live to fight another day."
            print ""
            return
        
    def _choice(self):
        print "To continue, you must go through the Shelob's Clef."
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = raw_input("Would you like to continue? Choices: 'yes' and 'no.' ")
        print ""
        return choice

    def _shelobClef(self, player):
        print "As you enter into Shelob's Clef, you are surrounded by a supernatural darkness and the stench of rotting corpses."
        raw_input("Press enter to continue. ")
        print ""
        
        if phialOfGaladriel in player.getInventory():
            print "Galadriel's phial lights up the entire chamber."
        
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        shelobAppearance = random.random()
        if shelobAppearance < .4:
            battle(player, constants.BattleEngineContext.STORY, self._wave)
            
        print "You encounter a thick spider web."
        raw_input("Press enter to hack through the web. ")
        print ""
        
        shelobAppearance = random.random()
        if shelobAppearance < .4:
            battle(player, constants.BattleEngineContext.STORY, self._wave)
        
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        shelobAppearance = random.random()
        if shelobAppearance < .4:
            battle(player, constants.BattleEngineContext.STORY, self._wave)
        
        print "You encounter a thick spider web."
        raw_input("Press enter to hack through the web. ")
        print ""
        
        shelobAppearance = random.random()
        if shelobAppearance < .4:
            battle(player, constants.BattleEngineContext.STORY, self._wave)
            
        print "...."
        raw_input("Press enter to continue. ")
        print ""
        
        shelobAppearance = random.random()
        if shelobAppearance < .4:
            battle(player, constants.BattleEngineContext.STORY, self._wave)
        
        print "You have emerged through the darkness!"
        raw_input("Press enter to continue. ")
        print ""
        
        self._cirithUngol(player)
    
    def _cirithUngol(self, player):
        successfulEscape = random.random()
        if successfulEscape < constants.UniquePlaceConstants.CirithUngolSneakProb:
            print "You manage to sneak through the Tower of Cirith Ungol and are now in the heart of Mordor."
            raw_input("Press enter to continue. ")
            print ""
        else:
            print "As you attempt to sneak through the rest of the passage, you are discovered by an orc patrol."
            raw_input("Press enter to continue. ")
            print ""
            
            battle(player, constants.BattleEngineContext.STORY, self._wave2)
            
            print "You make it into Mordor and Sauron has been alerted of your presence."
            raw_input("Press enter to continue. ")
            print ""