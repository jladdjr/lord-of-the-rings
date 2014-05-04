#!/usr/bin/python

class Place(object):
    """
    Parent class to both the City object and the UniquePlace object.
    """
    def __init__(self, name, description):
        """
        Initializes place object.

        @param name:           The name of the city.
        @param description:    A description of the city.
        """
        self._name = name
        self._description = description

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
