#!/usr/bin/python

from cities.building import Building

class Square(Building):
    """
    Squares are public spaces that allow players to interface with city folk.
    """
    def __init__(self, name, description, greetings, talk = None):
        """
        Initializes square object.

        @param name:           The name of the square.
        @param description:    A description of the square.
        @param greetings:      The greetings the user gets as he enters a square.
        @param talk:           A dictionary of people names and strings that are returned if a player talks in square.
        """
        Building.__init__(self, name, description, greetings)

        self._talk = talk
        
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
        TALK = 1
        LEAVE = 2
        
        choice = None
        while choice != LEAVE:
            print "There are %s people to talk to in %s:" % (numPeople, self._name)
            for person in self._talk:
                print "\t %s" % person
            print """
            What would you like to do:
            1) Talk to someone
            2) Leave
            """

            #Determine person player wants to talk to
            choice = int(raw_input("What is your choice? "))
            if choice == TALK:
                targetTalk = raw_input("Whom would you like to talk to? ")
                
                #Prints the string associated with that person
                if targetTalk in self._talk:
                    print ""
                    print self._talk[targetTalk] + "."
                    print ""
                    
                #If that person doesn't exist
                else:
                    print ""
                    print "Alas, %s could not be found in %s." % (targetTalk, self._name)
                    print ""
                    
            #The option to leave
            elif choice == LEAVE:
                print "Leaving %s." % self._name
                
            #For invalid choices
            else:
                print "Invalid choice."
                print ""
