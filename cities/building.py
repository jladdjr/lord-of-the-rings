#!/usr/bin/python

class Building(object):
    """
    A generic building object, used for inheritance.
    
    Building children include inns, shops, and squares.
    These classes have their own set of methods.
    """
    def __init__(self, name, description, greetings):
        """
        Initializes the building object.

        @param name:           The name of the building.
        @param description:    A description of the building.
        @param greetings:      The greetings the user gets as (s)he enters
                               building.
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
        Returns the string that is displayed as player enteres 
        the building.

        @return:    The greetings player receives upon entering
                    the building.
        """
        return self._greetings

    def enter(self, player):
        """
        Default enter method. By default, does nothing.

        This method should be overridden by child classes.

        @param player:   The player object.
        """
        pass