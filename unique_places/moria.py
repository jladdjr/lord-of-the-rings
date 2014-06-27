#!/usr/bin/python

from unique_place import UniquePlace
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.balrog import Balrog
from battle_engine import battle
from items.unique_items import phialOfGaladriel
import constants
import random

class Moria(UniquePlace):
    """
    An instance of UniquePlace.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize UniquePlace object.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.        
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)
        
        self._danger = 0
        
        self._sneak = ["You continue through narrow halls, seeking to avoid detection....", 
        "You creep by an rotting library....", 
        "You creep down a mine shaft....",
        "You sneak through some ancient tunnels....", 
        "You creep through a maze of machinery....", 
        "You sneak past a series of corpses....", 
        "You sneak past some strange glyphs...."]
        
        self._neutral = ["You find the staircase littered with the corpses of dwarven warriors.",
        "You pass an enormous mine shaft.",
        "You appear to be lost and turn back around.",
        "You find yourself in an enormous hall, ending an a winding staircase.",
        "You pass by what used to be a meeting place.",
        "You trust your gut in making a series of turns.",
        "You find yourself trapped and needing to turn around."]
        
        self._risk = ["You hear some footsteps....",
        "You think you see some shadows moving....",
        "You hear a series of agitated grunting....", 
        "You see shadows darting along in the distance....",
        "You hear whispers in the darkness...."]
        
        self._run = ["You run over some rotting corpses!",
        "You run past an endless stair!",
        "You dart along some minecarts!"
        "You run along a hall of columns!",
        "You run along a large mine shaft!",
        "You dart past some ancient tombs!"
        "You climb over a pile of rubble!"]
             
    def enter(self, player):
        """
        Enter Moria.
        
        @param player:   The current player.
        """
        pass
        """
        print self._greetings
        print ""
        
        print "You enter into a once-glorious hall, moving quickly in the shadows."
        raw_input("Press enter to continue." )
        print ""
        timeInMoria = random.randrange(15, 25)
        
        for time in range(timeInMoria):
            if self._danger < 3:
                random = random.random()
                if random < .3:
                    statement = random.choice(self._sneak)
                elif .3 <= random < .6:
                    statement = random.choice(self._neutral)
                else:
                    statement = random.choice(self._risk)
                    chanceBattle = random.random()
                    self._danger += 1
            elif 3 <= self._danger < 6:
                random = random.random()
                if random < .2:
                    statement = random.choice(self._sneak)
                elif .2 <= random < .5:
                    statement = random.choice(self._neutral)
                else:
                    statement = random.choice(self._risk)
                    self._danger += 1
            else:
                random = random.random()
                elif random < .3:
                    statement = random.choice(self._neutral)
                else:
                    statement = random.choice(self._risk)
                    self._danger += 1
                    
            print statement
            raw-input("Press enter to continue. ")
        
        print "Print you emerge from Moria into the light of day!"
        raw_input("Press enter to continue. ")
        print ""
        """