#!/usr/bin/python

from unique_place import UniquePlace
from items.potion import Potion
import constants

class Derningle(UniquePlace):
    """
    Derningle (or Fangorn Forest) is a unique place in Fangorn. 

    If player visits Derningle, he has the opportunity to interact with 
    Treebeard, gain items and experience.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Derningle.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        UniquePlace.__init__(self, name, description, greetings)

        #Create gift
        self._gift = []
        description = ("A mysterious elixir with extremely powerful" 
            " nourishing properties")
        for potion in range(3):
            potion = Potion("Ent Draught", description, 2, 42, 100)
            self._gift.append(potion)

    def enter(self, player):
        """
        Enter Derningle.

        @param player:  The current player.
        """
        #Story
        print self._greetings
        print ""
        print ("You find yourself deep within Fangorn Forest and it appears" 
            " as though the \ntrees are alive.")
        raw_input("Press enter to continue. ")
        print ""

        #Solicit user input for decision tree
        print "You find yourself at a fork in the woods."
        raw_input("Press enter to continue. ")
        print ""
        choice = self._fork()
        
        #Implement user choice
        if choice == "left":
            self._leftDestination(player)
        else:
            #Solicit user input for secondary decision tree
            choice = self._straightDestination()
            
            #Implement user choice
            if choice == "yes":
                self._continueDestination(player)
                print "You leave Fangorn blessed."
                print ""
            else:
                print ("You leave Fangorn in a hurry, feeling watched the" 
                " entire time.")
                print ""
            
    def _fork(self):
        """
        Solicits user input.
        """
        choice = None
        acceptable = ["left", "straight"]
        while choice not in acceptable:
            choice = raw_input("What would you like to do? Options: 'left' or" 
            " 'straight.' ")
        print ""
        
        return choice

    def _leftDestination(self, player):
        """
        Terminal destination given that player chooses to go 'right.' Here,
        player gets an experience bonus. 
        
        @param player:  The current player.
        """
        #Calculate experience increase
        experienceIncrease = (player.getExperience() * 
            constants.DERINGLE_EXP_INCREASE)
        
        #Story
        print ("You find yourself in a sunny pasture deep within the depths of"
        " Fangorn Forest.")
        raw_input("Press enter to continue. ")
        print ""
        
        print ("You realize that you are not only fighting for yourself but" 
        " for beautiful places \nsuch as this. Great strength wells up within" 
        " your inner man.")
        raw_input("Press enter to continue. ")
        print ""
        
        #Player gets experience increase
        print "Player gains %s experience." % experienceIncrease
        player.increaseExperience(experienceIncrease)
        raw_input("Press enter to continue. ")
        print ""

    def _straightDestination(self):
        """
        Potentially non-terminal destination given that user choose to go 
        'straight.' User is prompted to go continue deeper into the forest or 
        turn around.
        """
        #Story
        print ("You find yourself in a dark passage in Fangorn and you feel" 
            " uneasy. You hear \nrustling about.")
        raw_input("Press enter to continue. ")
        print ""
        
        #Solicit user choice
        choice = None
        acceptable = ["yes", "no"]
        while choice not in acceptable:
            choice = raw_input("Would you like to continue venturing deeper" 
                " into the forest? \nOptions: 'yes' or 'no.' ")
        print ""
        
        return choice

    def _continueDestination(self, player):
        """
        Terminal destination given that use picks 'straight' and 'yes.' Here, 
        player meets Treebeard and gets a gift.
               
        @param player:  The current player.
        """
        #Story
        print "You find yourself in an an opening surrounded by several ents!"
        raw_input("Press enter to continue. ")
        print ""

        print "Treebeard: \"Are you a little orc?\""
        raw_input("Press enter to continue. ")
        print ""

        print ("\"Ah I see. Please continue fighting for what is right and" 
            " receive this blessing \nfrom us.\"")
        raw_input("Press enter to continue. ")
        print ""
        
        #Player receives gift
        print ("\"Received three ent-draughts! These are legendary elixirs of" 
            " incredible power.\"")
        toRemove = []
        for item in self._gift:
            if player.addToInventory(item):
                toRemove.append(item)
        for item in toRemove:
            self._gift.remove(item)
        print ""