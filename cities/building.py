#!/usr/bin/python

class Building(object):
    """
    Generic Building object. Building children include Inns, Shops, and Squares.      
    These objects will also have their own special methods.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes building object.

        @param name:           The name of the building.
        @param description:    A description of the building.
        @param greetings:      The greetings the user gets as (s)he enters building.
        """
        self._name = name
        self._description = description
        self._greetings = greetings

    def getName(self):
        """
        Returns name of building.

        @return:    The name of the building.
        """
        return self._name
        
    def returnBuilding(self, name):
        """
        Returns the building object, given the name of the building.
        
        @param name:     The name of the building.
        
        @return:         The building object.
        """
        return self

    def getDescription(self):
        """
        Returns description of building.

        @return:    The description of the building.
        """
        return self._description

    def greetings(self):
        """
        Returns the string that represents player greeting upon entering building.

        @return:    The greetings player receives upon entering building.
        """
        return self._greetings

    def enter(self, player):
        """
        Default enter method. By default, does nothing.

        This method should be overridden by child class.

        @param player:   The player object.
        """
        pass
