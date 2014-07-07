#!/usr/bin/python

from unique_place import UniquePlace
from items.weapon import Weapon
from monsters.goblin import Goblin
from monsters.great_goblin import GreatGoblin
from battle_engine import battle
import constants

import random

class GoblinTown(UniquePlace):
    """
    GoblinTown is a unique place in High Pass. 
    
    The player has the opportunity to attempt to creep around 
    GoblinTown or to go straight in. If the attempt to sneak 
    is unsuccessful, player has to fight an enormous number of 
    monsters all at once.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes GoblinTown.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Spawn loot
        weapon = Weapon("Goblin Blade", "Good for goblins, terrible for humans", 1, 1, 1)
        weapon2 = Weapon("Dwarven Axe", "Stolen from Erebor", 1, 3, 1)
        weapon3 = Weapon("Poleaxe", "Looks Gondorian... represents stolen goods", 1, 3, 1)
        self._loot = [weapon, weapon2, weapon3]

        #Create three monster waves
        self._wave = []
        self._wave2 = []
        self._wave3 = []

        #Create monster wave #1
        for monster in range(2):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave.append(monster)
            
        #Create monster wave #2
        for monster in range(13):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave2.append(monster)

        #Create monster wave #3
        for monster in range(4):
            monster = Goblin(constants.MONSTER_STATS[Goblin])
            self._wave3.append(monster)
        monster = GreatGoblin(constants.MONSTER_STATS[GreatGoblin])
        self._wave3.append(monster)
    
        #Create monster wave #4
        self._wave4 = self._wave + self._wave2 + self._wave3

    def enter(self, player):
        """
        Action sequence for GoblinTown.

        @param player:  The current player.
        """
        print self._greetings
        print ""
        
        #Fight wave 1
        print "As you creep along High Pass hoping to avoid detection, you hear some creeping in the shadows...."
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, self._wave)
        if not result:
            return
            
        #Story
        print "You have defeated some unsuspecting goblins! Escaping detection now may still be an option."
        raw_input("Press enter to continue. ")
        print ""
    
        #Solicit user choice
        print "As you think ahead, you have two options. You may attempt to sneak through Gollum's Cave taking the risk getting trapped or go straight into Goblin Town."
        print ""
        choice = self._choice()

        #Run choice-dependent scripts
        if choice == "cave":
            self._cave(player)
        else:
            self._frontalAssault(player)
        
    def _choice(self):
        """
        Solicit user choice.
        
        @param player:  The current player.
        """
        choice = None
        acceptable = ["cave", "straight"]
        while choice not in acceptable:
            choice = raw_input("What would you like to do? Choices: try to sneak through the 'cave' or go 'straight' in. ")
        print ""
        
        return choice
        
    def _cave(self, player):
        """
        Action sequence for Gollum's cave.
        
        @param player:  The current player.
        """
        print "You try to sneak through Gollum's Cave."
        raw_input("Press enter to continue. ")
        print ""

        #If player ventures through undetected
        if random.random() < constants.UniquePlaceConstants.GoblinTownCaveEvasion:
            print "You make it through the mountains safely!"
            raw_input("Press enter to continue. ")
            print ""
            
        #If player gets  trapped in cave.
        else:
            #Story
            print "Great Goblin: \"You fool... did you really think you could make it through my territory without me knowing?\""
            raw_input("Press enter to continue. ")
            print ""
            
            #Fight wave 4
            print "Great Goblin: \"Now I will feast on your flesh....\""
            raw_input("Press enter to continue. ")
            print ""
            result = battle(player, constants.BattleEngineContext.STORY, self._wave4)
            if not result:
                return
            
            #Call victory sequence
            self._victorySequence(player)
            
    def _frontalAssault(self, player):
        """
        Action sequence for frontal assault choice.
        
        @param player:  The current player.
        """
        #Story
        print "Time to slay some goblins! On to Goblin Town!"
        raw_input("Press enter to continue. ")
        print ""
        
        print "You see some primitive huts, all uninhabited." 
        raw_input("Press enter to continue. ")
        print ""
        
        print "Suddenly, goblins circle you from all directions!"
        raw_input("Press enter to continue. ")
        print ""

        #Frontal assault wave 1
        print "Great Goblin: \"What makes you think that you can just charge into my city?\" "
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, self._wave2)
        if not result:
            return
            
        #Frontal assault wave 2
        print "Great Goblin: \"You stupid fool it is now time to DIE!\" "
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, self._wave3)
        if not result:
            return
            
        #Call victory sequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Victory sequence for making it through Goblin Town.
        
        @param player:  The current player.
        """
        print "As you gaze over the corpses of your enemies, you decide that it is time to take your winnings and leave."
        raw_input("Press enter to take loot. ")
        print ""

        #Give player items
        for item in self._loot:
            player.addToInventory(item)
        self._loot = []
        print ""
        
        self._createPort("south")