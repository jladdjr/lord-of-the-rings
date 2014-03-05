#!/usr/bin/python

import constants
from items.item import Item

class Armor(Item):
    """
    Armor class.
    """

    def __init__(self, name, description, weight, defense):
        """
        Initializes armor class.

        @param name:         The name of the item.
        @param description:  Armor description.
        @param weight:       Armor weight.
        @param defense:      The defense stat of the piece of armor.
        """
        Item.__init__(self, name, description, weight)
        self._defense = defense

    def getDefense(self):
        """
        Returns the item's defense stat.

        @return: Armor's defense.
        """
        return self._defense

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.ARMOR
