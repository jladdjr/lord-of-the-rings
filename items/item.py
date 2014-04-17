#!/usr/bin/python

from constants import ItemType

class Item(object):
    """
    A generic item. May be held by a player, exist in a room, etc.

    Direct use of this class is discouraged. Instead, create a 
    subclass of Item based on its type (e.g. Potion, Weapon, Armor).
    """
    def __init__(self, name, description, weight):
        """
        Initializes an item object.

        @param name:        Name of item.
        @param description: Description of item.
        @param weight:      Weight of item. (Must be positive integer)
        """
        if (not name) or (not description) or (not weight):
            raise AssertionError("Item must have name, description, and weight.")
        if weight < 1:
            errorMsg = "Invalid weight for item (%s); weight must be positive integer." % weight
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self._weight = weight

    def getName(self):
        """
        Gets item's name.

        @return: Item's name.
        """
        return self._name

    def getDescription(self):
        """
        Gets item's description.

        @return: Item's description.
        """
        return self._description

    def getWeight(self):
        """
        Gets item's weight.

        @return: Item's weight.
        """
        return self._weight

    def getType(self):
        """
        Returns the item's type.

        @attention: This method I{must} be overridden 
        by all subclasses of Item. (A new ItemType
        must also be defined in constants.py.)

        @return: Item's type.
        """
        return ItemType.GENERIC
