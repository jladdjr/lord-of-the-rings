#!/usr/bin/python

from constants import ItemType
from items.item import Item

class Armor(Item):
    """
    Armor class.
    """
    def __init__(self, name, description, weight, defense, cost):
        """
        Initializes armor class.

        @param name:         The name of the item.
        @param description:  Armor description.
        @param weight:       Armor weight.
        @param defense:      The defense stat of the piece of armor.
        """
        Item.__init__(self, name, description, weight)
        self._defense = defense
        self._cost = cost

    def getDefense(self):
        """
        Returns the item's defense stat.

        @return: Armor's defense.
        """
        return self._defense

    def getCost(self):
        """
        Returns armor cost.

        @return:    Armor cost
        """
        return self._cost

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.ARMOR
