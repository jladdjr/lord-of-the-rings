#!/usr/bin/python

from unique_place import UniquePlace
from monsters.nazgul import Nazgul
from battle_engine import battle
from items.weapon import Weapon
from items.armor import Armor
from items.item import Item
import constants
import random

class Tharbad(UniquePlace):
    """
    Tharbad is a unique place in Mitheithel. It is the remains of an city that 
    was once inhabited by men.
    
    Here the user is given the option of exploring the ruins. Exploring the 
    ruins grants the player the ability to find items at the risk of a chance 
    encounter with Nazgul.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Tharbad.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Generates list of Nazgul that user may fight
        self._monsters = []
        numberNazgul = random.randrange(0, 5)
        for monster in range(numberNazgul):
            nazgul = Nazgul(constants.MONSTER_STATS[Nazgul])
            self._monsters.append(nazgul)

        #Generate loot
        description = "Ancient runes and symbols"
        scroll = Item("Ancient Scroll", description, 0, 0)
        description = "Looks like it can break at any second"
        weapon = Weapon("Rotting Staff", description, 1, 1, 1)
        description = "Maybe one or two hits and it's through"
        armor = Armor("Rotting Shield", description, 1, 1, 1)
        self._loot = [scroll, weapon, armor]
        
    def enter(self, player):
        """
        Enter Tharbad.

        @param player:  The current player.
        """
        #Story
        print self._greetings
        print ""
        
        print ("You gaze upon the ancient ruins of the once great city of" 
            " Tharbad and see some very strange sights.")
        raw_input("Press enter to continue. ")
        print ""

        #Solicit user input
        choice = None
        acceptable = ["explore", "leave"]
        while choice not in acceptable:
            choice = raw_input("What would you like to do? Choices: 'explore'"
                " and 'leave.' ")
            print ""
        
        #Execute user-dependent scripts
        if choice == "explore":
            self._explore(player)
        else:
            print ("You bid farewell to the ruins of Tharbad and continue on" 
                " your journey.")
            print ""

    def _explore(self, player):
        """
        Action sequence for exploring Tharbad.

        @param player:   The player object.
        """
        #Solicit user input
        choice = None
        acceptable = ["ruined mill", "ancient bridge"]
        while choice not in acceptable:
            choice = raw_input("Where would you like to explore? Options:"
                " 'ruined mill' and 'ancient bridge.' ")
        print ""

        #If user chooses to explore ruined mill
        if choice == "ruined mill":
            print ("You find lots of rotting instruments and the remains of"
                " farming equipment.")
            raw_input("Press enter to continue. ")
            print ""
            self._itemFind(player)
            self._chanceBattle(player)

        #If user choose to explore ancient bridge
        elif choice == "ancient bridge":
            print ("You find the ruins of the ancient North-South Road bridge"
                " crossing. This was \nonce one of the greatest causeways in all"
                " of Middle Earth.")
            raw_input("Press enter to continue. ")
            print ""
            self._itemFind(player)
            self._chanceBattle(player)

        #Give player option to keep exploring
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = raw_input("Would you like to keep exploring? Options:"
                " 'yes' and 'no.' ")
        print ""
        
        if choice == "yes":
            self._explore(player)
        else:
            print "You leave Tharbad with a sense of loss."
            print ""
            
    def _chanceBattle(self, player):
        """
        Determines if a random battle is to occur."
        
        @param player:   The player object.
        """
        if random.random() < constants.UniquePlace.TharbadBattleProb:
            print "You hear some rustling in the shadows...."
            raw_input("Press enter to continue. ")
            print ""
            result = battle(player, constants.BattleEngineContext.STORY, 
                self._monsters)
            if not result:
                return
            
    def _itemFind(self, player):
        """
        Determines if player finds an item and then gives player that item.
        
        @param player:   The player object.
        """
        #If there are no items to find
        if len(self._loot) == 0:
            return
        
        chance = random.random()
        #Determines if player finds item and which item player receives
        if chance < constants.UniquePlace.TharbadItemFindProb:
            print "You find something that may be of some value!"
            item = random.choice(self._loot)
            if player.addToInventory(item):
                self._loot.remove(item)
            print ""