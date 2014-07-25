#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul_ii import Nazgul_II
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from monsters.witch_king import WitchKing
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

class MinasMorgul(UniquePlace):
    """
    Minas Morgul is a unique place in ephelDuath. In Tolkien's universe, it is 
    a city captive by witchcraft and home to the Nazgul.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Minas Morgul.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)
        
        self._wave = []
        self._wave2 = []
        self._wave3 = []
        
        #Create monster wave #1
        for monster in range(13):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave.append(monster)
        for monster in range(8):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(7):
            monster = Troll(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(8):
            monster = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave2.append(monster)
        monster = WitchKing(constants.MONSTER_STATS[WitchKing])
        self._wave2.append(monster)
        
        #Create monster wave #3
        for monster in range(7):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave3.append(monster)
        for monster in range(3):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave3.append(monster)
        for monster in range(4):
            monster = Nazgul_II(constants.MONSTER_STATS[Nazgul_II])
            self._wave3.append(monster)
        
        #Create loot
        description = "Seems to have a mind of its own"
        weapon = Weapon("Morgul Blade", description, 5, 0, 0)
        description = "Rusted over"
        weapon2 = Weapon("Morgul Blade", description, 4, 0 ,0)
        description = "Completely useless"
        armor = Armor("Rotting Shield", description, 5, 0, 0)
        description = "Too small for a human"
        armor2 = Armor("Travel Boots", description, 4, 0, 0)
        description = "Strange ingredients"
        potion = Potion("Orcish Tea", description, 1, 0, 2)
        description = "Of questionable health value"
        potion2 = Potion("Orcish Tea", description, 1, 0, 2)
        description = "Of potential value on the free market"
        item = Item("Orcish Banister", description, 1, 0)
        self._loot = [weapon, weapon2, armor, armor2, potion, potion2, item]
        
    def enter(self, player):
        """
        Action sequence for Minas Morgul.
        
        @param player:   The current player.
        """
        #Story
        print self._greetings
        print ""
        print "The haunted city of Minas Morgul chills your bones."
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
        Solicit user choice.
        
        @return:      User choice.
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
        Battle sequence for Minas Morgul.
        
        @param player:   The current player.
        """
        #Wave 1
        print ("Witch-King: \"Time for tea and crumpets. Please keep to the" 
            " left and don't \ntouch any of the artifacts.\" ")
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave)
        if not result:
            return
        
        print "Witch-King: \"Hmm. You appear to not like my tea. How Rude....\"" 
        raw_input("Press enter to continue. ")
        print ""
        
        #Wave 2
        print "Witch-King: \"Perhaps you will like this instead....\""
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave2)
        if not result:
            return
            
        #Call _victorySequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        """
        Victory sequence for Minas Morgul.
        
        @param player:   The current player.
        """
        print ("You have taken the city of Minas Morgul and secured the" 
            " western route into Mordor!")
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print "You quickly loot the battle field."
            raw_input("Press enter to continue. ")
            print ""
            for item in self._loot:
                if player.addToInventory(item):
                    self._loot.remove(item)
            print ""
        
        print "You quickly move on, knowing that Sauron is on the move too."
        print ""
        
        self._createPort("east")
        
    def _run(self, player):
        """
        The action sequence if player chooses to run. In this instance, player 
        still gets attacked by a smaller wave of enemies while leaving.
        
        @param player:   The current player.
        """
        #Battle enemies
        print ("As you rush out of the area, a large number of enemies catch" 
        " up to you.")
        raw_input("Press enter to continue. ")
        print ""
        result = battle(player, constants.BattleEngineContext.STORY, 
            self._wave3)
        if not result:
            return
            
        print "You narrowly escape your enemies."
        print ""