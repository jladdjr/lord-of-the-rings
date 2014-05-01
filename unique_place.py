#!/usr/bin/python

from place import Place

class UniquePlace(Place):
    """
    A unique place on the map. Different from cities, but exists within a space.
    """
    def __init__(self, name, description, greeting):
        """
        Initialize UniquePlace object.
        
        @param name:           The name of the UniquePlace.
        @param description:    A description of the UniquePlace.
        """
        Place.__init__(self, name, description, greeting)
