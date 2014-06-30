#!/usr/bin/python

from unique_place import UniquePlace
from battle_engine import battle
from items.item import Item
from items.weapon import Weapon
from items.armor import Armor
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
        "You run past an spiral staircase!",
        "You dart along some minecarts!",
        "You dash along a hall of columns!",
        "You dash along a large mine shaft!",
        "You dart past some ancient tombs!",
        "You climb over a pile of rubble!"]
        
        weapon = Weapon("Rusty Axe", "Taken from a slain dwarven warrior", 1, 1, 1)
        weapon2 = Weapon("Durin's Hammer", "Durin's legendary sword", 1, 1, 1)
        weapon3 = Weapon("Aeowyln", "A legendary spear", 1, 1, 1)
        weapon4 = Weapon("Durnhammer", "A mithril hammer", 1, 1, 1)
        armor = Armor("Iron Cap", "Old but still effective", 1, 1, 1)
        armor2 = Armor("Boots of Travel", "May increase magic find", 1, 1, 1)
        item = Item("Mithril", "One of Middle Earth's rarest metals", 1)
        item2 = Item("Ancient Runes", "Magical properties?", 1)
        self._loot = [weapon, weapon2, weapon3, weapon4, armor, armor2, item, item2]
        
    def enter(self, player):
        """
        Enter Moria.
        
        @param player:   The current player.
        """
        print self._greetings
        print ""
        
        print "You enter into a once-glorious hall, moving quickly among the shadows."
        raw_input("Press enter to continue. ")
        print ""
        
        #Generate length of time spent in Moria
        timeInMoria = random.randrange(15, 25)

        #Player journeys through Moria
        for time in range(timeInMoria):
            if self._danger < 1:
                result = self._lowRiskTravel(player)
            elif 1 <= self._danger < 3:
                result = self._mediumRiskTravel(player)
            else:
                result = self._highRiskTravel(player)
            
            #Unpack results
            statement = result[0]
            battleOccurence = result[1]
                        
            #Execute action sequence
            print statement
            raw_input("Press enter to continue. ")
            print ""
            
            if battleOccurence:
                print "BATTLE HAS OCCURRED."
                battle(player, constants.BattleEngineContext.RANDOM)
        
        #Ending sequence
        print "You emerge from Moria into the light of day!"
        raw_input("Press enter to continue. ")
        print ""
        
    def _lowRiskTravel(self, player):
        chance = random.random()
        if chance < .65:
            statement = random.choice(self._sneak)
            battle = False
            self._itemFind(player)
        elif .65 <= chance < .9:
            statement = random.choice(self._neutral)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._risk)
            self._danger += 1
            battle = True
        
        return statement, battle
            
    def _mediumRiskTravel(self, player):
        chance = random.random()
        if chance < .3:
            statement = random.choice(self._sneak)
            battle = False
            self._itemFind(player)
        elif .3 <= chance < .7:
            statement = random.choice(self._neutral)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._risk)
            self._danger += 1
            battle = True
               
        return statement, battle
            
    def _highRiskTravel(self, player):
        chance = random.random()
        if chance < .2:
            statement = random.choice(self._neutral)
            battle = False
            self._itemFind(player)
        else:
            statement = random.choice(self._run)
            self._danger += 1
            battle = True
        
        return statement, battle
        
    def _itemFind(self, player):
        chance = random.random()
        if self._loot and chance < .3:
            item = random.choice(self._loot)
            print "You found %s while venturing through the Mines of Moria!" % item.getName()
            
            player.addToInventory(item)
            self._loot.remove(item)
            
            raw_input("Press enter to continue. ")
            print ""