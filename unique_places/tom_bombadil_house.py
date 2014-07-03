#!/usr/bin/python

from unique_place import UniquePlace
from items.weapon import Weapon
from items.potion import Potion

class TomBombadilHouse(UniquePlace):
    """
    TomBombadil's House is a unique place in Old Forest. In Tokien's 
    universe, Tom Bombadill is a mysterious mystic whose identity and 
    purpose is never fully explained.
    
    If the player visits Tom Bombadil, he gets a chance to dialogue 
    and receive some items.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Tom Bombadil's House.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)
        
        #Spawn loot
        weapon = Weapon("Walking Cane", "Has a secret, sharpened edge", 3, 3, 3)
        potion = Potion("Forest Tonic", "Contains rare herbs", 1, 3, 2)
        self._gift = [weapon, potion]
        
    def enter(self, player):
        """
        Allows the user to dialogue with Tom Bombadil and receive gifts.

        @param player:  The current player.
        """
        #Story
        print self._greetings
        print ""
        
        print "\"I am Tom Bombadil. My wife Goldberry and I live in these forests.\""
        raw_input("Press enter to continue. ")
        print ""
        
        print "\"I can tell that you are on a long journey and are carrying something that must be kept safe. I would like to leave you with a gift if you would like to accept it.\""
        raw_input("Press enter to continue. ")
        print ""
        
        #Give player loot
        for item in self._gift:
            player.addToInventory(item)
            self._gift.remove(item)
        print ""
        
        print "\"Thank you for visiting me in these forests.\""
