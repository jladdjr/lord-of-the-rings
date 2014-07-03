#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.black_numernorian import BlackNumernorian
from monsters.mouth_of_sauron import MouthOfSauron
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

class Isenmouthe(UniquePlace):
    """
    Isenmouthe is a unique place in Udun. In Tolkien's universe it represents a
    scaled-down version of the Black Gate.
    
    If player visits Isenmouthe, he has the opportunity to break through to the 
    Plateau of Gorgoth (the heart of Mordor).
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Isenmouthe.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)
        
        self._wave = []
        self._wave2 = []
        
        #Create monster wave #1 
        for monster in range(14):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(7):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(6):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        for monster in range(3):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(5):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave2.append(monster)
        for monster in range(4):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave2.append(monster)
        for monster in range(2):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave2.append(monster)
        for monster in range(5):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave2.append(monster)
        for monster in range(4):
            monster = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._wave2.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave2.append(monster)
        
        #Create loot
        weapon = Weapon("Troll Hammer", "Enormous and unwieldy", 1, 1, 1)
        armor = Armor("Troll Shield", "Enormous and unwieldy", 4, 0, 0)
        potion = Potion("Orc Draught", "Disgusting", 1, 0, 2)
        potion2 = Potion("Orc Draught", "Potentially toxic", 1, 0, 2)
        item = Item("Orcish Banister", "Perhaps of high resale value", 1)
        item2 = Item("Screw and bolts", "Useless", 1)
        self._loot = [weapon, armor, potion, potion2, item, item2]
        
    def enter(self, player):
        """
        Action sequence for Isenmouthe.
        
        @param player:   The current player.
        """
        print self._greetings
        print ""
        print "You see several armies approaching as you near the Isenmouthe."
        raw_input("Press enter to continue. ")
        print ""
        
        #Run battle action sequence
        self._battle(player)
        
    def _battle(self, player):
        """
        Battle sequence for Isenmouthe.
        
        @param player:   The current player.
        """
        #Wave 1
        print "Mouth of Sauron: \"You have overstayed your welcome.\""
        raw_input("Press enter to continue. ")
        print ""
        battle(player, constants.BattleEngineContext.STORY, self._wave)
        
        #Wave 2
        print "Mouth of Sauron: \"Time... to... DIE!!!\""
        raw_input("Press enter to continue. ")
        print ""
        battle(player, constants.BattleEngineContext.STORY, self._wave2)
        
        #Call victory sequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Victory sequence for Isenmouthe.
        
        @param player:   The current player.
        """
        print "You have secured the north-west route into Mordor!"
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print "While looting the battlefield, you find strange items."
            raw_input("Press enter to continue.")
            print ""
            for item in self._loot:
                player.addToInventory(item)
            self._loot = []
            print ""
        
        print "Welcome to the heart of Mordor!"
        print ""