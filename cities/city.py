#!/usr/bin/python

class City(object):
    """
    Cities are the towns of the game. Cities may have inns, blacksmiths and people to talk to.
    """
    def __init__(self, name, description, greetings, buildings = None):
        """
        Initializes city object.

        @param name:           The name of the city.
        @param description:    A description of the city.
        @param greetings:      The greetings the user gets as he enters a city.
        @param talk:           What the local say when the user talks to the locale.
        """
        self._name = name
        self._description = description
        self._greetings = greetings
        self._buildings = buildings

    def getName(self):
        """
        Returns name of city.

        @return:    The name of the city.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of city.

        @return:    The description of the city.
        """
        return self._description

    def greetings(self):
        """
        Prints a screen that represents a player greeting upon entering city.
        """
        print self._greetings
        
    def getBuildings(self):
        """
        Returns list of building objects.
        """
        return self._buildings
