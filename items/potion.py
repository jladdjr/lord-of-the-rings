#!/usr/bin/python

from constants import ItemType
from items.item import Item

class Potion(Item):
    """
    A class of potions. Potions have the defining parameter, healing. 
    """
    def __init__(self, name, description, weight, healing, cost):
        """
        Initializes potions class.

        @param name:          Name of portion.
        @param description:   Description of potion.
        @param weight:        Weight of weapon.
        @param healing:       Healing stat of weapon. Player heals by the maximum
                              of this amount when player uses potion.
        """
        Item.__init__(self, name, description, weight)
        self._healing = healing
        self._cost = cost

    def getHealing(self):
        """
        Returns the potion's healing stat.

        @return: Potion's healing stat.
        """
        return self._healing

    def getCost(self):
        """
        Returns the potion's cost.

        @return: The cost of potion.
        """
        return self._cost

    def getType(self):
        """
        Returns the item's type.

        @return: Item's type.
        """
        return ItemType.POTION
