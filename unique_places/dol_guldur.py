#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.black_numernorian import BlackNumernorian
from monsters.witch_king import WitchKing
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

import random

class DolGuldur(UniquePlace):
    """
    An instance of UniquePlace.
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
        
        self._wave = []
        self._wave2 = []
        self._wave3 = []
        
        #Create monster wave #1 
        for monster in range(11):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(10):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(7):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        
        #Create monster wave #2
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._wave2.append(nazgul)
        if random.random() < constants.UniquePlaceConstants.DolGuldurWitchKingProb:
            witchKing = WitchKing(constants.MONSTER_STATS[WitchKing])
            self._wave2.append(witchKing)
        for monster in range(8):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave2.append(monster)
            
        #Create monster wave #3
        numberNazgul = random.randrange(0, 8)
        for monster in range(numberNazgul):
            nazgul = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._wave2.append(nazgul)
        for monster in range(6):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave3.append(monster)
        self._wave3.append(monster)
        
        #Create loot
        weapon = Weapon("Cursed Sword", "Fills you with fear", 5, 0, 0)
        weapon2 = Weapon("Cursed Axe", "You lose confidence holding this", 5, 0, 0)
        armor = Armor("Cursed Shield", "Gaping holes", 5, 0, 0)
        potion = Potion("Cursed Elixir", "An unknown substance", 1, 0, 2)
        item = Item("Cursed Mirror", "Odd distortions and shadows", 1)
        item2 = Item("Cursed Books", "Grimoires", 1)
        self._loot = [weapon, weapon2, armor, potion, item, item2]
        
    def enter(self, player):
        """
        Enter BlackGate.
        
        @param player:   The current player.
        """
        print self._greetings
        print ""
        
        choice = self._choice()
        
        #If player chooses to frontal assault
        if choice == "frontal assault":
            self._frontalAssault(player)
            
        #If player chooses to escape
        if choice == "escape":
            self._run(player)
            
    def _choice(self):
        choice = None
        acceptable = ["frontal assault", "escape"]
        while choice not in acceptable:
            choice = raw_input("What do you want to do? Choices: 'frontal assault' or 'escape.' ")
        print ""
        return choice
        
    def _frontalAssault(self, player):
        battle(player, constants.BattleEngineContext.STORY, self._wave)
        battle(player, constants.BattleEngineContext.STORY, self._wave2)
        
        #Call _victorySequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        print "Although you have taken the tower of Dol Guldur, a deep sense of evil still lingers over the land."
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print "While looking around, you find several items."
            raw_input("Press enter to continue.")
            print ""
            for item in self._loot:
                player.addToInventory(item)
            self._loot = []
            print ""
        
        print "You leave with a sense of foreboding."
        print ""
        
    def _run(self, player):
        print "You find yourself surrounded."
        raw_input("Press enter to continue. ")
        print ""
        
        battle(player, constants.BattleEngineContext.STORY, self._wave3)

        print "You escape with your life!"
        print ""