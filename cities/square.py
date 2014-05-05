#!/usr/bin/python

from cities.building import Building

class Square(Building):
    """
    Squares are public spaces that allow players to interface with city folk.
    """
    def __init__(self, name, description, greetings, talk = None, items = None):
        """
        Initializes square object.

        @param name:           The name of the square.
        @param description:    A description of the square.
        @param greetings:      The greetings the user gets as he enters a square.
        @param talk:           A dictionary of people names and strings that are returned if a player talks in square.
        """
        Building.__init__(self, name, description, greetings)

        self._talk = talk
        self._items = items
        
    def enter(self, player):
        """
        The events sequence upon player entering square.
        """
        numPeople = len(self._talk)

        print ""
        print "- - - %s - - -" % self._name
        print self._greetings
        print ""

        #User prompt
        choice = None
        while choice != "quit":
            print "There are %s people to talk to in %s:" % (numPeople, self._name)
            for person in self._talk:
                print "\t %s" % person

            choice = raw_input("\nWhom would you like to talk to ('quit' to quit)? ")

            #The option to leave
            if choice == "quit":
                print "Leaving %s." % self._name

            #If person exists
            elif choice in self._talk:
                print ""
                print self._talk[choice] + "."
                
                #If item still in self._items, give player item
                if self._items[choice]:
                    item = self._items[choice]
                    print "Received %s from %s" % (item.getName(), choice)
                    player.addToInventory(item)
                    self._items[choice] = None
                print ""
                    
            #If person doesn't exist
            elif choice not in self._talk:
                print ""
                print "Alas, '%s' could not be found in %s." % (choice, self._name)
                print ""
                
            #For invalid choices
            else:
                print "Huh?"
                print ""
