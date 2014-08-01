#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
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

class BlackGate(UniquePlace):
    """
    The Black Gate is a unique place in Dead Marshes.
    
    The Black Gate is the most obvious way into Mordor. If player visits the 
    Black Gate, he is given the option of either fighting his way though the 
    Gate or running. If he chooses to fight, he has to fight wave upon wave of 
    enemies to gain access into the next space. If he chooses to run, he still 
    has to fight a smaller amount of enemies.
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
        
        self._wave = []
        self._wave2 = []
        self._wave3 = []
        self._wave4 = []
        
        #Create monster wave #1 
        for monster in range(11):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(6):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(6):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        for monster in range(2):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(12):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave2.append(monster)
        for monster in range(8):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave2.append(monster)
        for monster in range(4):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave2.append(monster)
        for monster in range(9):
            monster = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave2.append(monster)
            
        #Create monster wave #3
        for monster in range(6):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave3.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave3.append(monster)
         
        #Create monster wave #4 
        for monster in range(8):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave4.append(monster)
        for monster in range(5):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave4.append(monster)
        for monster in range(3):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave4.append(monster)
        for monster in range(4):
            monster = BlackNumernorian(constants.MONSTER_STATS[BlackNumernorian])
            self._wave4.append(monster)
        
        #Create loot
        weapon = Weapon("Orcish Knife", "Jagged and old", 4, 12, 8)
        armor = Armor("Rotting Boots", "Completely useless", 4, 0, 0)
        potion = Potion("Orc Draught", "May contain human flesh", 2, 0, -15)
        potion2 = Potion("Orc Draught", 
            "Basically the orcish version of Gatorade", 2, 0, -10)
        item = Item("Orcish Pillow", "Basically, a rock", 3, 0)
        item2 = Item("Orcish Blankets", "For slumber parties", 4, 2)
        self._loot = [weapon, armor, potion, potion2, item, item2]
        
    def enter(self, player):
        """
        The Black Gate's action sequence.
        
        @param player:   The player object.
        """
        #Story
        print self._greetings
        print ""
        print ("\"Several armies rise up to meet you as you approach the Black" 
            " Gate.\"")
        raw_input("Press enter to continue. ")
        print ""
        
        #Solicit user choice
        choice = self._choice()
        
        #If player chooses to frontal assault
        if choice == "frontal assault":
            self._frontalAssault(player)
            
        #If player chooses to run
        if choice == "run":
            self._run(player)
            
    def _choice(self):
        """
        Determines if user wants to attack or run.
        """
        choice = None
        acceptable = ["frontal assault", "run"]
        while choice not in acceptable:
            choice = raw_input("What do you want to do? Choices: 'frontal" 
                " assault' or 'run.' ")
        print ""
        
        return choice
        
    def _frontalAssault(self, player):
        """
        The action sequence if the user decides to attack the Black Gate.
        
        @param player:   The player object.
        """
        #Battle wave 1
        print "Mouth of Sauron: \"I'm so glad you came! Slumber party!\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave)
        if not result:
            return
            
        #Battle wave 2
        print "Mouth of Sauron: \"Hmm. You appear to not like our house.\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return
            
        #Battle wave 3
        print "Mouth of Sauron: \"Time to DIE!\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return
            
        #Call the victory sequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        The victory sequence for securing the Black Gate.
        
        @param player:   The player object.
        """
        #Story
        print ("You have taken the Black Gate and secured part of the" 
            " north-western route into \nMordor!")
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print "While looting the battlefield, you find many items."
            raw_input("Press enter to continue. ")
            print ""
            for item in self._loot:
                if player.addToInventory(item):
                    self._loot.remove(item)
            print ""
        
        #Story
        print "You continue your quest for better night-time entertainment."
        print ""
        
        self._createPort("east")
        
    def _run(self, player):
        """
        The action sequence given that the player tries to run. In this 
        instance, a smaller chunk of enemies catch up to the player.
        
        @param player:   The player object.
        """
        #Battle wave 4
        print "The leading army catches up with you." 
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave4)
        if not result:
            return
            
        #Story
        print "You escape the rest of your pursuers!"
        print ""