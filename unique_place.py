#!/usr/bin/python

from place import Place

class UniquePlace(Place):
    """
    A unique place inherits from the Place parent class.
    A unique place on the map. Different from cities, but exists within a space.
    """
        
    def __init__(self, name, description):
        """
        Initialize UniquePlace object.
        
        @param name:           The name of the UniquePlace.
        @param description:    A description of the UniquePlace.
        """
        #Call parent class init function
        Place.__init__(self, name, description)
    
    def enter(self, player):
        """
        Enter unique place.

        @param player:  The current player.
        """
        print "Hello, and welcome to %s" % self._name
