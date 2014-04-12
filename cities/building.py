#!/usr/bin/python

class Building(object):
    """
    Generic Building object. Inns, Shops, Squares, etc. inherit from the Building object.      
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

    def getDescription(self):
        """
        Returns description of building.

        @return:    The description of the building.
        """
        return self._description

    def greetings(self):
        """
        Prints a screen that represents a player greeting upon entering building.

        @return:    The greetings player receives upon entering building.
        """
        return self._greetings

    #TODO: Create enter() method here.
    #      Leave it empty, but in the docstring mention that
    #      it should be overwritten by the child class.
    #      This helps developers know that the enter() method
    #      is something all sub-classes of building should
    #      have in common.

    def enterBuilding(self, player):
        """
        This method should be overridden by every child class.

        @player:    The player.
        """
        print "This method should be overwritten."
