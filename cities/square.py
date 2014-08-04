#!/usr/bin/python

from cities.building import Building
from items.item import Item

class Square(Building):
    """
    Squares are children of Building and inhabit cities.
    
    Squares serve as public spaces that allow players to
    interface with city folk.
    """
    def __init__(self, name, description, greetings, talk = None, 
    items = None):
        """
        Initializes square object.

        @param name:           The name of the square.
        @param description:    A description of the square.
        @param greetings:      The greetings the user gets as he enters a 
                               square.
        @param talk:           A dictionary of names-responses used for 
                               dialogue.
        @param items:          Items that the player may receive for talking 
                               to people.
        """
        Building.__init__(self, name, description, greetings)

        self._talk = talk
        self._items = items
        
    def enter(self, player):
        """
        The action sequence for square.
        
        @param player:     The player object.
        """
        print ""
        print "- - - %s - - -" % self._name
        print self._greetings
        print ""

        #If square is empty
        if self._talk == None:
            print "You find %s completely deserted." % self._name
            return

        #User prompt
        numPeople = len(self._talk)
        
        choice = None
        while choice != "quit":
            print "There are %s people to talk to in %s:" % (numPeople, 
            self._name)
            for person in self._talk:
                print "\t %s" % person

            prompt = "\nWhom would you like to talk to ('quit' to quit)? "
            choice = raw_input(prompt)

            #The option to leave
            if choice == "quit":
                print "Leaving %s." % self._name

            #If person exists
            elif choice in self._talk:
                print ""
                print self._talk[choice]

                #If target person has items
                if choice in self._items:
                    gift = self._items[choice]
                    self._giveItem(player, choice)
                print ""
                    
            #If person doesn't exist
            else:
                print ""
                print "Alas, '%s' could not be found in %s." % (choice, 
                self._name)
                print ""
                
    def _giveItem(self, player, choice):
        """
        Helper method that is responsible for handing player receiving items.
        
        @param player:  The player object.
        @param gift:    The gift that player is supposed to receive.
        @param choice:  The person that the user has chosen to talk to.
        """
        gift = self._items[choice]
        
        #If entry is single item
        if isinstance(gift, Item):
            if player.addToInventory(gift):
                print "Received %s from %s." % (gift.getName(), choice)
                del self._items[choice]
            
        #If entry is a list
        elif isinstance(gift, list):
            successfulItems = []
            for item in gift:
                if player.addToInventory(item):
                    print "Received %s from %s." % (item.getName(), choice)
                    successfulItems.append(item)
                    
            #Cleanup
            if successfulItems == gift:
                del self._items[choice]
            for item in successfulItems:
                gift.remove(item)