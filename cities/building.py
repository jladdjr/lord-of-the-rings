#!/usr/bin/python

class Building(object):
    """
    Generic Building object. Inns, Shops, Squares, etc. inherit from the Building object.      
    These objects will also have their own special methods.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes Building object.

        @param name:           The name of the building.
        @param description:    A description of the building.
        @param greetings:      The greetings the user gets as (s)he enters a building.
        """
        
        self._name = name
        self._description = description
        self._greetings = greetings

    def getName(self):
        """
        Returns name of inn.

        @return:    The name of the inn.
        """
        return self._name

    def getDescription(self):
        """
        Returns description of inn.

        @return:    The description of the inn.
        """
        return self._description

    def greetings(self):
        """
        Prints a screen that represents a player greeting upon entering inn.
        """
        return self._greetings
