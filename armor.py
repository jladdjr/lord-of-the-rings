#!/usr/bin/python

import constants
from items.item import Item

class Armor(Item):
    """
    Armor class.
    """

    def __init__(self, defense, name, description, weight):
        """
        Initializes armor class.

        @param defense:      The defense stat of the piece of armor.
        @param name:         The name of the item.
        @param description:  Armor description.
        @param weight:       Armor weight.
        """
        Item.__init__(self, name, description, weight)
        self.defense = defense

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.ARMOR
