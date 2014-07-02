#!/usr/bin/python

from place import Place

class UniquePlace(Place):
    """
    A unique place inherits from the Place parent class.
    A unique place on the map. Different from cities, but exists within a space.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize UniquePlace object.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:	The greetings the user gets as he enters the inn.
        """
        #Call parent class init function
        Place.__init__(self, name, description, greetings)
    
    def enter(self, player):
        """
        Enter unique place.

        @param player:  The current player.
        """
        print self._greetings
