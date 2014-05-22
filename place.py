#!/usr/bin/python

class Place(object):
    """
    Parent class to both the city object and the unique place object.
    """
    def __init__(self, name, description, greetings):
        """
        Initialize place object.
        
        @param name:           The name of the Place.
        @param description:    A description of the Place.
        @param greetings:      The greetings upon entering place.
        """
        self._name = name
        self._description = description
        self._greetings = greetings
    
    def getName(self):
        """
        Returns name of place.

        @return:    The name of the place.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of place.

        @return:    The description of the place.
        """
        return self._description

    def getGreeting(self):
        """
        Returns the greetings of place
        """
        return self._greetings

    def enter(self, player):
        """
        Parent enter method. Should we overridden by children classes.
        
        @param player:  The current player.
        """
        print "This enter method should be overridden by child class"
