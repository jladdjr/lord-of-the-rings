#!/usr/bin/python

from constants import ItemType

class Item(object):
    """
    A generic item. May be held by a player, exist in a room, etc.

    Item has various child classes such as Weapon and Armor.
    """
    def __init__(self, name, description, weight, cost):
        """
        Initializes an item object.

        @param name:          Name of item.
        @param description:   Description of item.
        @param weight:        Weight of item.
        """
        if (not name) or (not description):
            raise AssertionError("Item must have a name and description.")
        if weight < 0:
            errorMsg = "Invalid weight for item (%s); weight cannot be a negative number." % weight
            raise AssertionError(errorMsg)
        if cost < 0:
            errorMsg = "Invalid cost for item (%s); cost cannot be a negative number." % cost
            raise AssertionError(errorMsg)

        self._name = name
        self._description = description
        self._weight = weight
        self._cost = cost

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
        
    def getCost(self):
        """
        Returns weapon cost.

        @return:    Weapon cost.
        """
        return self._cost

    def getType(self):
        """
        Returns the item's type.

        @attention: This method I{must} be overridden 
        by all subclasses of Item. (A new ItemType
        must also be defined in constants.py.)

        @return: Item's type.
        """
        return ItemType.GENERIC
