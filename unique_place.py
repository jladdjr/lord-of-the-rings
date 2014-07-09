#!/usr/bin/python

from place import Place

class UniquePlace(Place):
    """
    Inherits from the Place parent class.
    
    A unique place on the map. May have any number of features, 
    including battles and story interaction.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize UniquePlace object.
        
        @param name:            The name of the UniquePlace.
        @param description:     A description of the UniquePlace.
        @param greetings:       The greetings the user gets as he enters.
        """
        #Call parent class init function
        Place.__init__(self, name, description, greetings)
    
    def enter(self, player):
        """
        Enter unique place.

        @param player:  The current player.
        """
        print self._greetings