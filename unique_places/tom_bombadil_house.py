#!/usr/bin/python

from unique_place import UniquePlace
from items.weapon import Weapon
from items.potion import Potion

class TomBombadilHouse(UniquePlace):
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

        weapon = Weapon("Walking Cane", "Has a secret, sharpened edge", 3, 3, 3)
        potion = Potion("Forest Tonic", "Contains rare herbs", 1, 3, 2)
        self._gift = [weapon, potion]
        
    def enter(self, player):
        """
        Enter Tom Bomadil's House.

        @param player:  The current player.
        """
        print self._greetings
        print ""
        print "\"I am Tom Bombadil. My wife Goldberry and I live in these forests.\""
        raw_input("Press enter to continue. ")
        print ""
        print "\"I can tell that you are on a long journey and are carrying something that must be kept safe. I would like to leave you with a gift if you would like to accept it.\""
        raw_input("Press enter to continue. ")
        print ""
        for item in self._gift:
            player.addToInventory(item)
            self._gift.remove(item)
        print ""
        print "\"Thank you for visiting me in these forests.\""
