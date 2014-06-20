#!/usr/bin/python

from unique_place import UniquePlace
from items.potion import Potion
import constants

class Derningle(UniquePlace):
    """
    Derningle is also known as Fangorn Forest, where ents
    live.

    If player visits Derningle, he has the opportunity to interact
    with Treebeard, gain items and experience.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Derningle.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
	@param greetings:	The greetings the user gets as he enters.        
	"""
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Spawn gift
        self._gift = []
        for potion in range(3):
            potion = Potion("Ent Draught", "A mysterious elixir with extremely powerful nourishing properties", 1, 10, 5)
            self._gift.append(potion)

    def enter(self, player):
        """
        Enter Derningle.

        @param player:  The current player.
        """
	print self._greetings
	print ""
        print "You find yourself deep within Fangorn Forest and it appears as though the trees are alive."
        raw_input("Press enter to continue. ")
        print ""

        print "You find yourself at a fork in the woods."
        raw_input("Press enter to continue. ")
        print ""
        choice = self._fork()
        
        if choice == "left":
            self._leftDestination(player)
        else:
            choice = self._straightDestination()
            
            if choice == "yes":
                self._continueDestination(player)
                print "You leave Fangorn blessed."
                print ""
            else:
                print "You leave Fangorn in a hurry, feeling watched the entire time."
                print ""
            
    def _fork(self):
        choice = None
        acceptable = ["left", "straight"]
        while choice not in acceptable:
            choice = raw_input("What would you like to do? Options: 'left' or 'straight.' ")
        print ""
        return choice

    def _leftDestination(self, player):
        experienceIncrease = player.getExperience() * constants.UniquePlaceConstants.DeringleExperienceIncrease

        print "You find yourself in a sunny pasture deep within the depths of Fangorn Forest."
        raw_input("Press enter to continue. ")
        print ""
        
        print "You realize that you are not only fighting for yourself but for beautiful places such as this. Great strength wells up within your inner man."
        raw_input("Press enter to continue. ")
        print ""
        
        print "Player gains %s experience." % experienceIncrease
        player.increaseExperience(experienceIncrease)
        raw_input("Press enter to continue. ")
        print ""

    def _straightDestination(self):
        print "You find yourself in a dark passage in Fangorn and you feel uneasy. You hear rustling about."
        raw_input("Press enter to continue. ")
        print ""

        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = raw_input("Would you like to continue venturing deeper into the forest? Options: 'yes' or 'no.' ")
        print ""
        
        return choice

    def _continueDestination(self, player):
        print "You find yourself in an an opening surrounded by several ents!"
        raw_input("Press enter to continue. ")
        print ""

        print "Treebeard: \Are you a little orc?\""
        raw_input("Press enter to answer. ")
        print ""

        print "\"Ah I see. Please continue fighting for what is right and receive this blessing from us.\""
        raw_input("Press enter to receive. ")
        print ""

        print "\"Received three ent-draughts! These are legendary elixirs of incredible power.\""
        for item in self._gift:
            player.addToInventory(item)
        self._gift = []
        print ""
