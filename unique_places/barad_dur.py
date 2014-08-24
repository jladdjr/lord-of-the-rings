#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_iii import Nazgul_III
from monsters.orc_ii import Orc_II
from monsters.orc_archer_ii import OrcArcher_II
from monsters.troll_ii import Troll_II
from monsters.black_numernorian_ii import BlackNumernorian_II
from monsters.dragon_of_mordor import DragonOfMordor
from monsters.witch_king import WitchKing
from monsters.mouth_of_sauron import MouthOfSauron
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

class BaradDur(UniquePlace):
    """
    Barad Dur is a unique place in Plateau of Gorgoth.
    
    Barad Dur is an enormous fortress that that the player really has no
    reason to visit. If he visits, he encounters wave after wave of enemies.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize Barad Dur.
        
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
        self._wave5 = []
        
        #Create monster wave #1 
        for monster in range(12):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave.append(monster)
        for monster in range(7):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave.append(monster)
        for monster in range(5):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave.append(monster)
        for monster in range(3):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(15):
            monster = Orc_II(constants.MONSTER_STATS[Orc_II])
            self._wave2.append(monster)
        for monster in range(6):
            monster = OrcArcher_II(constants.MONSTER_STATS[OrcArcher_II])
            self._wave2.append(monster)
        for monster in range(10):
            monster = Troll_II(constants.MONSTER_STATS[Troll_II])
            self._wave2.append(monster)
        for monster in range(4):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave2.append(monster)
            
        #Create monster wave #3
        for monster in range(5):
            monster = BlackNumernorian_II(constants.MONSTER_STATS[BlackNumernorian_II])
            self._wave3.append(monster)
        monster = MouthOfSauron(constants.MONSTER_STATS[MouthOfSauron])
        self._wave3.append(monster)
         
        #Create monster wave #4 
        for monster in range(8):
            monster = Nazgul_III(constants.MONSTER_STATS[Nazgul_III])
            self._wave4.append(monster)
        monster = WitchKing(constants.MONSTER_STATS[WitchKing])
        self._wave4.append(monster)
            
        #Create monster wave #5
        for monster in range(14):
            monster = DragonOfMordor(constants.MONSTER_STATS[DragonOfMordor])
            self._wave5.append(monster)
            
        #Create loot
        potion = Potion("Hyper Potion", "Extreme healing qualities", 2, 112, 
            500)
        potion2 = Potion("Super Potion", "Medium healing qualities", 2, 76, 350)
        potion3 = Potion("Dragon Milk", "Healing qualities", 2, 142, 1000)
        item = Item("Masterball", "Can catch any Pokemon", 4, 272)
        item2 = Item("Moonstone", "Evolves normal Pokemon", 6, 196)
        item3 = Item("Nugget", "High resale value", 12, 5000)
        self._loot = [potion, potion2, potion3, item, item2, item3]
        
    def enter(self, player):
        """
        Barad Dur's action sequence.
        
        @param player:   The player object.
        """
        #Story
        print self._greetings
        print ""
        print ("A host of figures rise up to meet you as you approach Barad"
            " Dur.")
        raw_input("Press enter to continue. ")
        print ""
        
        #Calls the battle sequence
        self._battle(player)
        
    def _battle(self, player):
        """
        Barad Dur's battle sequence. Player fights five waves of enemies.
        
        @param player:   The player object.
        """
        print "Orc Commander I: \"We're having a blast upstairs! Slumber party!\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave)
        if not result:
            return
            
        print ("Orc Commander II: \"Didn't you read the sign? No %ss" 
            " allowed.\"" % player.getName())
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return
            
        print "Mouth of Sauron: \"You want ANOTHER slumber party?!\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return
            
        print "Nazgul: \"AAAAEEEEEEEEEEE!!!\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave4)
        if not result:
            return
            
        print ("Lance of the Elite Four: \"I've been waiting for you, %s! I" 
            " knew \nthat you, with your skills, would eventually reach me here.\"" 
            % player.getName())
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave5)
        if not result:
            return
            
        #Call _victorySequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Barad Dur's victory sequence. Player gets loot.
        
        @param player:   The player object.
        """
        #Story
        print "You have defeated Lance, the Pokemon League champion!"
        raw_input("Press enter to continue. ")
        print ""
        
        print "Congratulations on your accomplishments!"
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print ("While looting the battlefield, you find several" 
                " interesting items. The tower itself remains locked, however.")
            raw_input("Press enter to continue. ")
            print ""
            
            toRemove = []
            for item in self._loot:
                if player.addToInventory(item):
                    toRemove.append(item)
            for item in toRemove:
                self._loot.remove(item)
            print ""
        
        #Story
        print "You set off for other ventures within the Dark Land."
        raw_input("Press enter to leave. ")
        print ""