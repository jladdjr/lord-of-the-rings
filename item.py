#!/usr/bin/python

class Item(object):
    """
    A generic item. May be held by a player or exist in a room.
    """

    def __init__(self, name, description, weight):
        """
        Initializes an item object.

        @param name:        Name of item
        @param description: Description of item
        @param weight:      Weight of item
        """
        self._name =        name
        self._description = description
        self._weight =      weight

    def getName(self):
        """
        Gets item's name.

        @return: Item's name.
        """
        return self._name

    def getDescription(self):
        """
        Get's item's description.

        @return: Item's description
        """
        return self._description

    def getWeight(self):
        """
        Get's item's weight.

        @return: Item's weight.
        """
        return self._weight


