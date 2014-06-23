#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from monsters.orc import Orc
from monsters.orc_archer import OrcArcher
from monsters.troll import Troll
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.potion import Potion
from items.item import Item
import constants

class MinasMorgul(UniquePlace):
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
        for monster in range(4):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave.append(monster)
        for monster in range(6):
            monster = Orc(constants.MONSTER_STATS[Troll])
            self._wave.append(monster)
        
        #Create monster wave #2
        for monster in range(9):
            monster = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._wave2.append(monster)
            
        #Create monster wave #3
        for monster in range(7):
            monster = Orc(constants.MONSTER_STATS[Orc])
            self._wave3.append(monster)
        for monster in range(3):
            monster = OrcArcher(constants.MONSTER_STATS[OrcArcher])
            self._wave3.append(monster)
        for monster in range(4):
            monster = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._wave3.append(monster)
        
        #Create loot
        weapon = Weapon("Morgul Blade", "Seems to have a mind of its own", 5, 0, 0)
        weapon2 = Weapon("Morgul Blade", "Rusted over", 4, 0 ,0)
        armor = Armor("Rotting Shield", "Completely useless", 5, 0, 0)
        armor2 = Armor("Travel Boots", "Too small for a human", 4, 0, 0)
        potion = Potion("Orcish Tea", "Strange ingredients", 1, 0, 2)
        potion2 = Potion("Orcish Tea", "Of questionable health value", 1, 0, 2)
        item = Item("Orcish Banister", "Of potential value on the free market", 1)
        self._loot = [weapon, weapon2, armor, armor2, potion, potion2, item]
        
    def enter(self, player):
        """
        Enter Minas Morgul.
        
        @param player:   The current player.
        """
        print self._greetings
        print ""
        print "Down to some business! Minas Morgul is a haunted fortress-city that is home to the Nazgul and hosts a huge garrison."
        raw_input("Press enter to continue. ")
        print ""
        
        choice = self._choice()
        
        #If player chooses to frontal assault
        if choice == "frontal assault":
            self._frontalAssault(player)
            
        #If player chooses to run
        if choice == "run":
            self._run(player)
            
    def _choice(self):
        choice = None
        acceptable = ["frontal assault", "run"]
        while choice not in acceptable:
            choice = raw_input("What do you want to do? Choices: 'frontal assault' or 'run.' ")
        print ""
        return choice
        
    def _frontalAssault(self, player):
        print "Witch-King: \"Time for tea and crumpets. Please keep to the left and don't touch any of the artifacts.\" "
        raw_input("Press enter to continue. ")
        print ""
        
        battle(player, constants.BattleEngineContext.STORY, self._wave)
        
        print "Witch-King: \"Hmm. You appear to not like my tea. How Rude....\"" 
        raw_input("Press enter to continue. ")
        print ""
        
        print "Witch-King: \"Perhaps you will like this instead....\""
        raw_input("Press enter to continue. ")
        print ""
        
        battle(player, constants.BattleEngineContext.STORY, self._wave2)
        
        #Call _victorySequence
        self._victorySequence(player)
        
    def _victorySequence(self, player):
        print "You have taken the city of Minas Morgul and secured the western route into Mordor!"
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        if len(self._loot) != 0:
            print "You quickly loot the battle field."
            raw_input("Press enter to continue.")
            print ""
            for item in self._loot:
                player.addToInventory(item)
            self._loot = []
            print ""
        
        print "You quickly move on, knowing that Sauron is on the move too."
        print ""
        
    def _run(self, player):
        print "As you rush out of the area, a large number of enemies catch up to you." 
        raw_input("Press enter to continue. ")
        print ""
        
        battle(player, constants.BattleEngineContext.STORY, self._wave3)

        print "You narrowly escape your enemies."
        print ""
