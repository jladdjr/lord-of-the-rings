#!/usr/bin/python

from cities.building import Building

class Inn(Building):
    """
    Inns are in cities. Inns allow player to heal.
    """
    def __init__(self, name, description, greetings, cost):
        """
        Initializes inn object.

        @param name:           The name of the inn.
        @param description:    A description of the inn.
        @param greetings:      The greetings the user gets as he enters a inn.
        @param cost:           The cost of using the inn.
        """
        Building.__init__(self, name, description, greetings)
        self._cost = cost
        
    def execute(self, player):
        """
        Executes inn object.
        """
        print self._greetings
        print "Cost to stay: %s." %self._cost
    
    def getCost(self):
        """
        Returns cost for using inn.
        
        @return:    Cost of using inn.
        """
        return self._cost
